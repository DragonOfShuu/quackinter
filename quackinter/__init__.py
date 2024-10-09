from quackinter.quackinter import interpret
from quackinter.interpreter import Interpreter

from quackinter.errors import (
    QuackinterError,
    InterpretationError,
    CommandNotDefinedError,
    OutsideContextError,
    NotANumberError
)

__all__ = [
    "interpret",
    "Interpreter",
    "QuackinterError",
    "InterpretationError",
    "CommandNotDefinedError",
    "OutsideContextError",
    "NotANumberError"
]
