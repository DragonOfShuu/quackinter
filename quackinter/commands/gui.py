from quackinter.commands.command import Command
from quackinter.context import Context
from quackinter.key_injector import KeyInjector


class GUI(Command):
    names = ["GUI", "WINDOWS"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str):
        injector = KeyInjector(context)
        injector.hotkey(['win', *data.strip().split(' ')])