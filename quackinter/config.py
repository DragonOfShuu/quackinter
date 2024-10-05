from dataclasses import dataclass


@dataclass
class Config:
    delay: float = 0
    interval: float = 0.1
