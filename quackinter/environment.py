from __future__ import annotations
from typing import Any

from quackinter.commands.command import Command
from quackinter.config import Config


class Environment:
    """
    A class that stores variables that
    gets and sets, whilst also allowing
    you to create extensions of the heap.
    """
    def __init__(self, previous_env: Environment|None = None):
        self.previous_env = previous_env
        self.vars: dict[str, Any] = {}
        if self.previous_env:
            self.global_vars = self.previous_env.global_vars
        else:
            self.global_vars: dict[str, Any] = {}

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
    
    def init(self, commands: list[Command], config: Config):
        """
        Initialize the given commands, and have
        this be the global environment.
        """
        for cmd in commands:
            cmd.global_environment_init(self, config)
