from quackinter.commands.command import Command
from quackinter.context import Context
from quackinter.key_injector import KeyInjector


class StringLn(Command):
    names = ["STRINGLN"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        injector = KeyInjector(context)
        injector.write(f"{data}\n")