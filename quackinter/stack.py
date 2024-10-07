from quackinter.commands.command import Command
from quackinter.config import Config
from quackinter.context import Context
from quackinter.sanitizer import Sanitizer
from quackinter.utils import extract_cmd
from quackinter.errors import CommandNotDefinedError


class Stack:
    def __init__(self, commands: list[Command], config: Config) -> None:
        self.commands = commands
        self.config = config

    def run(self, ducky: list[str]) -> str | None:
        clean_ducky = Sanitizer.sanitize_lines(ducky)
        context = Context(clean_ducky)
        for i in context:
            cmd_str, data = extract_cmd(i[1])
            command = self._find_command(cmd_str, data)
            if not command:
                raise CommandNotDefinedError(i[0], context)

            command.execute(context, cmd_str, data)

    def _find_command(self, cmd: str, data: str) -> Command | None:
        for i in self.commands:
            if i.is_this_command(cmd, data):
                return i
        # Readability
        return None
