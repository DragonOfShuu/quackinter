from quackinter.commands.command import Command
from quackinter.commands import commands as built_in_ducky_commands
from quackinter.config import Config


class Stack:
    def __init__(
        self, commands: list[Command] | None = None, config: Config | None = None
    ) -> None:
        self.commands = built_in_ducky_commands if not commands else commands
        self.config = Config() if not config else config

    def run(self, ducky: list[str]) -> str | None:
        pass
