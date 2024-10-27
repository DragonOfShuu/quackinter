from quackinter.commands.command import Command
from quackinter.stack import Stack
from quackinter.key_injector import KeyInjector


class StringLnCommand(Command):
    names = ["STRINGLN"]

    @classmethod
    def execute(cls, stack: Stack, cmd: str, data: str) -> None:
        injector = KeyInjector(stack.config)
        injector.write(f"{data}\n")
