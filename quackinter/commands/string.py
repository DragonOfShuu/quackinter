from quackinter.commands.command import Command
from quackinter.stack import Stack
from quackinter.key_injector import KeyInjector


class StringCommand(Command):
    names = ["STRING"]

    def execute(self, stack: Stack, cmd: str, data: str) -> None:
        injector = KeyInjector(stack.environment)
        injector.write(f"{data}")
