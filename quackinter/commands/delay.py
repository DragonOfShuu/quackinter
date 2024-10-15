from time import sleep

from quackinter.commands.command import Command
from quackinter.stack_context import StackContext


class Delay(Command):
    names = ["DELAY"]

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        sleep(cls.convert_float(data))
