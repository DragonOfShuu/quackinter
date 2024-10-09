from quackinter.commands.command import Command
from quackinter.context import Context
import pyautogui as pyag


class StringLn(Command):
    names = ["STRINGLN"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        pyag.write(f"{data}\n", interval=context.config.char_interval)
