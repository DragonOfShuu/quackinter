from quackinter.commands.command import Command
from quackinter.stack_context import StackContext
from quackinter.key_injector import KeyInjector


class String(Command):
    names = ["STRING"]

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        injector = KeyInjector(context)
        injector.write(f"{data}")
