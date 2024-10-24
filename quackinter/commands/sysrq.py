from quackinter.commands.command import Command
from quackinter.stack_context import StackContext

from quackinter.key_injector import KeyInjector


class SysRqCommand(Command):
    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        key_injector = KeyInjector(context)
        key_injector.hotkey(["alt", "prntscrn", data.strip()])
