from quackinter.commands.command import Command
from quackinter.context import Context


class Rem(Command):
    names = ["REM"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        context.config.output(data)
