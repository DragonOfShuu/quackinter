from quackinter.commands.command import Command
from quackinter.config import Config
from quackinter.context import Context
from quackinter.sanitizer import Sanitizer


class Stack:
    def __init__(self, commands: list[Command], config: Config) -> None:
        self.commands = commands
        self.config = config

    def run(self, ducky: list[str]) -> str | None:
        clean_ducky = Sanitizer.sanitize_lines(ducky)
        context = Context(clean_ducky)
        for i in context:
            pass
