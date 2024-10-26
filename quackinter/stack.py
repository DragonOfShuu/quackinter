from __future__ import annotations

from quackinter.commands.command import Command
from quackinter.environment import Environment
from quackinter.stack_context import StackContext
from quackinter.sanitizer import Sanitizer
from quackinter.utils import extract_cmd
from quackinter.errors import CommandNotDefinedError, InterpretationError


class Stack:
    def __init__(
        self,
        environment: Environment,
    ) -> None:
        self.config = environment.config
        self.context: StackContext | None = None
        self.old_enviro = environment
        if environment:
            self.environment = environment.extend()
        else:
            self.environment = Environment()

    def run(self, ducky: list[str]) -> str | None:
        clean_ducky = Sanitizer.sanitize_lines(ducky)
        self.context = StackContext(clean_ducky, self.environment, self)
        for i in self.context:
            cmd_str, data = extract_cmd(i.line)
            command = self._find_command(cmd_str, data)

            try:
                if not command:
                    raise CommandNotDefinedError(f"{cmd_str} is not a command.")

                command.execute(self.context, cmd_str, data)
            except InterpretationError as ie:
                ie.add_context(self.context)
                raise ie

    def _find_command(self, cmd: str, data: str) -> Command | None:
        for i in self.environment.commands:  # type: ignore
            if i.is_this_command(cmd, data):
                return i
        return None

    def new_stack(self):
        return Stack(self.environment)
