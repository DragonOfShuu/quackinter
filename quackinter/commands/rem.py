from quackinter.commands.command import Command
from quackinter.stack import Stack


class RemCommand(Command):
    names = ["REM"]

    @classmethod
    def execute(cls, stack: Stack, cmd: str, data: str) -> None:
        stack.config.output(data)
