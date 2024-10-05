from abc import ABC, abstractmethod

from quackinter.context import Context

class Command(ABC):
    name = 'base'

    @abstractmethod
    @staticmethod
    def execute(context: Context):
        pass