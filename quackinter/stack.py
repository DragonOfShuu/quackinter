from __future__ import annotations

from quackinter.commands.command import Command
from quackinter.config import Config
from quackinter.environment import Environment
from quackinter.stack_context import StackContext
from quackinter.sanitizer import Sanitizer
from quackinter.utils import extract_cmd
from quackinter.errors import CommandNotDefinedError, InterpretationError


class Stack:
    def __init__(
        self,
        commands: list[Command],
        config: Config,
        old_enviro: Environment | None = None,
    ) -> None:
        self.commands = commands
        self.config = config
        self.context: StackContext | None = None
        self.old_stack = old_enviro
        if old_enviro:
            self.environment = old_enviro.extend()
        else:
            self.environment = Environment()

    def run(self, ducky: list[str]) -> str | None:
        clean_ducky = Sanitizer.sanitize_lines(ducky)
        self.context = StackContext(clean_ducky, self.config)
        for i in self.context:
            cmd_str, data = extract_cmd(i[1])
            command = self._find_command(cmd_str, data)
            if not command:
                raise CommandNotDefinedError(i[0], self.context)

            try:
                command.execute(self.context, cmd_str, data)
            except InterpretationError as ie:
                ie.add_context(self.context)
                raise ie

    def _find_command(self, cmd: str, data: str) -> Command | None:
        for i in self.commands:
            if i.is_this_command(cmd, data):
                return i
        # Readability
        return None
