from quackinter.commands.command import Command
from quackinter.interpreter import Interpreter
from quackinter.stack import Stack

from tests.testing_tools.make_command import make_command

# import pytest
from time import perf_counter


def hello_world_cmd(global_list: list[str]):
    def execute(command_self: Command, stack: Stack, cmd: str, data: str):
        global_list.append("Hello World")

    return make_command(["HELLO_WORLD"], execute)


def test_simple_interpretation():
    global_list = []

    simple_command = hello_world_cmd(global_list)

    interpreter = Interpreter([simple_command], False)
    interpreter.interpret_text("HELLO_WORLD\n\n")

    assert global_list == ["Hello World"]


def test_speed_interpretation():
    global_list = []

    simple_command = hello_world_cmd(global_list)

    start = perf_counter()
    interpreter = Interpreter([simple_command])
    interpreter.interpret_text("HELLO_WORLD\n" * 50000)
    end = perf_counter()

    assert global_list == ["Hello World" for _ in range(50000)]
    assert end - start < 1
