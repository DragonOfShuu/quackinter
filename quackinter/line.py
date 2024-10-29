from dataclasses import dataclass

from quackinter.commands.command import Command


@dataclass
class Line:
    line: str
    line_index: int
    orig_line: str
    command: Command | None = None
