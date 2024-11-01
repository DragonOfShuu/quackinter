from typing import Any, Protocol, TYPE_CHECKING

from quackinter.commands.command import Command
from quackinter.stack import Stack

if TYPE_CHECKING:
    from quackinter.stack import Stack


class ExecuteCommand(Protocol):
    @staticmethod
    def __call__(command_self: Command, stack: "Stack", cmd: str, data: str) -> Any: ...


def make_command(new_names: list[str], new_execute: ExecuteCommand):
    class TestCommand(Command):
        names = new_names

        def execute(self, stack: Stack, cmd: str, data: str) -> None:
            return new_execute(self, stack, cmd, data)

    return TestCommand
