from abc import ABC, abstractmethod

from quackinter.context import Context
from quackinter.errors import NotANumberError


class Command(ABC):
    names = ["BASE"]

    @classmethod
    @abstractmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        pass

    @classmethod
    def is_this_command(cls, name: str, data: str) -> bool:
        return name.upper() in cls.names

    @staticmethod
    def convert_float(data: str):
        try:
            return float(data)
        except ValueError:
            raise NotANumberError(f"Value '{data}' is not a float.")

    @staticmethod
    def convert_int(data: str):
        try:
            return int(data)
        except ValueError:
            raise NotANumberError(f"Value '{data}' is not an integer.")
