from quackinter.commands.command import Command
from quackinter.commands import commands as built_in_ducky_commands


class Stack:
    def __init__(self, ducky: list[str], commands: list[Command]|None = None) -> None:
        self._ducky_code = ducky
        self.commands = built_in_ducky_commands if not commands else commands

    def run(self) -> str|None:
        pass
    