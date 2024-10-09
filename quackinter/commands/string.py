from quackinter.commands.command import Command
from quackinter.context import Context
import pyautogui as pyag


class String(Command):
    names = ["STRING"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        pyag.write(f"{data}", interval=context.config.char_interval)
