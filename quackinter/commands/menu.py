from quackinter.commands.command import Command
from quackinter.context import Context
from quackinter.key_injector import KeyInjector


class Menu(Command):
    names = ["APP", "MENU"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        injector = KeyInjector(context)
        injector.hotkey(['apps', *data.strip().split(' ')])
