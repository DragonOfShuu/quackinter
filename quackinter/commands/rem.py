from quackinter.commands.command import Command
from quackinter.stack_context import StackContext


class RemCommand(Command):
    names = ["REM"]

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        context.config.output(data)
