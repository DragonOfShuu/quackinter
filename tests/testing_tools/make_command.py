from typing import Any, Protocol, TYPE_CHECKING

from quackinter.commands.command import Command
from quackinter.stack import Stack

if TYPE_CHECKING:
    from quackinter.stack import Stack


class ExecuteCommand(Protocol):
    def __call__(self, stack: "Stack", cmd: str, data: str) -> Any: ...


def make_command(new_names: list[str], new_execute: ExecuteCommand):
    class TestCommand(Command):
        names = new_names

        def execute(self, stack: Stack, cmd: str, data: str) -> None:
            return new_execute(stack, cmd, data)

    return TestCommand
