from quackinter.commands.command import Command
from quackinter.stack_context import StackContext

from pymsgbox import alert


class WaitForButtonPressCommand(Command):
    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        alert(data.strip(), button="CONTINUE")
