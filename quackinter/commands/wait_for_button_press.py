from quackinter.commands.command import Command
from quackinter.stack import Stack

from pymsgbox import alert


class WaitForButtonPressCommand(Command):
    def execute(self, stack: Stack, cmd: str, data: str) -> None:
        alert(data.strip(), button="CONTINUE")
