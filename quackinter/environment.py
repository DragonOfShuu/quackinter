from __future__ import annotations
from typing import Any

from quackinter.commands.command import Command
from quackinter.config import Config
from quackinter.errors import EnvironmentNotIniatedError


class Environment:
    """
    A class that stores variables that
    gets and sets, whilst also allowing
    you to create extensions of the heap.
    """

    def __init__(self, previous_env: Environment | None = None):
        self.previous_env = previous_env
        self.vars: dict[str, Any] = {}
        if self.previous_env:
            self.global_vars: dict[str, Any] = self.previous_env.global_vars
            self.commands: list[Command]|None = self.previous_env.commands
            self.config: Config|None = self.previous_env.config
        else:
            self.global_vars = {}
            self.commands = None
            self.config = None

    def edit_var(self, name: str, val: Any) -> bool:
        """
        Edit a variable on the enviro stack,
        starting here and going down.
        """
        if name in self.vars:
            self.vars[name] = val
            return True
        if self.previous_env:
            return self.previous_env.edit_var(name, val)
        return False

    def add_var(self, name: str, val: Any) -> bool:
        """
        Add a var, or editing a variable
        lower in the stack.
        """
        successful_edit = self.edit_var(name, val)
        if successful_edit:
            return False

        self.vars[name] = val
        return True

    def remove_var(self, name: str) -> bool:
        """
        Remove a variable from the environment,
        starting with this point in the enviro
        stack, going down
        """
        if name in self.vars:
            self.vars.pop(name)
            return True

        if self.previous_env:
            return self.previous_env.remove_var(name)

        return False

    def extend(self):
        """
        Extend this environment by returning
        a new environment.
        """
        return Environment(self)

    def _global_init(self, commands: list[Command], config: Config):
        """
        Initialize the given commands, and have
        this be the global environment.
        """
        self.commands = commands
        for cmd in self.commands:
            cmd.global_environment_init(self, config)
    
    def _global_exit(self):
        if self.commands is None or self.config is None: 
            raise EnvironmentNotIniatedError("Environment was supposed to exit but instead does not exist.") 
        for cmd in self.commands:
            cmd.global_environment_exit(self, self.config)

    @classmethod
    def create_global(cls, commands: list[Command], config: Config):
        new_global = cls()
        new_global._global_init(commands, config)
        return new_global

    def __enter__(self):
        if self.previous_env is None:
            return
    
    def __exit__(self, exc_type: type[Exception], exc_value: str, exc_traceback: str):
        # General environment closing statement

        if self.previous_env is None:
            self._global_exit()
