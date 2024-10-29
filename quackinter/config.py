from dataclasses import dataclass
from typing import Protocol


class OutputPrint(Protocol):
    def __call__(self, output: str): ...


@dataclass
class Config:
    # Delay before we start
    delay: float = 0
    # Interval between lines
    interval: int | None = None
    # Interval between chars
    char_interval: int = 80
    # In case we need to print somewhere,
    # where to print
    output: OutputPrint = lambda output: None
