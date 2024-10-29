from quackinter.commands.command import Command
from quackinter.stack import Stack
from quackinter.key_injector import KeyInjector


class StringLnCommand(Command):
    names = ["STRINGLN"]

    def execute(self, stack: Stack, cmd: str, data: str) -> None:
        injector = KeyInjector(stack.environment)
        injector.write(f"{data}\n")
