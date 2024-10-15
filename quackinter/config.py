from dataclasses import dataclass
from typing import Protocol


class OutputPrint(Protocol):
    def __call__(self, output: str): ...


@dataclass
class Config:
    delay: float = 0
    interval: int | None = None
    char_interval: int = 80
    output: OutputPrint = lambda output: None
