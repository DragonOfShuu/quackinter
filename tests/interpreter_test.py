from quackinter.config import Config
from quackinter.interpreter import Interpreter
from tests import hello_world_cmd

# import pytest
from time import perf_counter


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


def test_delay():
    config = Config(delay=300, output=lambda output: print(output))
    interpreter = Interpreter(config=config)
    start = perf_counter()
    interpreter.interpret_text("PRINTLN hello world")
    end = perf_counter()

    assert end - start > 0.3
    assert end - start < 0.301
