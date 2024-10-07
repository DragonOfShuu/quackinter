from abc import ABC, abstractmethod

from quackinter.context import Context


class Command(ABC):
    names = ["BASE"]

    @abstractmethod
    @staticmethod
    def execute(context: Context, cmd: str, data: str) -> None:
        pass

    @classmethod
    def is_this_command(cls, name: str, data: str) -> bool:
        return name.upper() in cls.names
