from time import sleep

from quackinter.commands.command import Command
from quackinter.stack import Stack


class DelayCommand(Command):
    names = ["DELAY"]

    @classmethod
    def execute(cls, stack: Stack, cmd: str, data: str) -> None:
        sleep(cls.convert_float(data))
