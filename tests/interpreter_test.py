from quackinter.config import Config
from quackinter.environment import Environment
from tests.testing_tools.make_command import make_command

from quackinter.stack import Stack


def test_simple_interpretation():
    make_it_list = []

    def execute(stack: Stack, cmd: str, data: str):
        make_it_list.append("Hello World")

    simple_command = make_command(["HELLO_WORLD"], execute)

    with Environment.create_global([simple_command], Config()) as global_env:
        new_stack = Stack(global_env)
        new_stack.run(["HELLO_WORLD"])

    assert make_it_list == ["Hello World"]
