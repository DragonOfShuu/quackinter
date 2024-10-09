from dataclasses import dataclass
from typing import Protocol


class OutputPrint(Protocol):
    def __call__(self, output: str):
        ...

@dataclass
class Config:
    delay: float = 0
    interval: float|None = None
    char_interval: float = 0.08
    output: OutputPrint = lambda output: None
    