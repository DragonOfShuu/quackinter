from time import sleep

from quackinter.commands.command import Command
from quackinter.context import Context

class Delay(Command):
    names = ["DELAY"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        sleep(cls.convert_float(data))
        