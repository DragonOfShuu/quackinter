from quackinter.commands.command import Command
from quackinter.interpreter import Interpreter
from quackinter.stack import Stack
from tests import hello_world_cmd, make_command

import pytest
from typing import cast


@pytest.mark.parametrize("line_offset", [(0), (5), (2)])
def test_generated_lines(line_offset: int):
    hello_world = hello_world_cmd([])

    # ducky_code = [[(f"HELLO_WORLD {i}" if i != 2) for i in range(5)], "READ_BACK"]
    ducky_code: list[str] = cast(
        list[str],
        """HELLO_WORLD 0
HELLO_WORLD 1
HELLO_WORLD 2


HELLO_WORLD 3
HELLO_WORLD 4
READ_BACK""".split(
            "\n"
        ),
    )

    def execute_read_back(command_self: "Command", stack: "Stack", cmd: str, data: str):
        stack_context = stack.context
        empty_lines = 2

        assert len(stack_context.generated_lines) == 6
        assert stack_context.current_line_num == line_offset + 6 + empty_lines

        back_one_line = stack_context.get_line_offset(1)
        assert back_one_line is not None, "The previous line must not be None"
        assert isinstance(back_one_line.command, hello_world)
        assert back_one_line.line == "HELLO_WORLD 4"
        assert back_one_line.line_num == line_offset + 5 + empty_lines

    read_back = make_command(["READ_BACK"], execute_read_back)

    def execute_imposter(command_self: "Command", stack: "Stack", cmd: str, data: str):
        """
        Create an imposter stack
        """
        new_stack = stack.new_stack()
        new_stack.run(ducky_code, line_offset)

    imposter = make_command(["IMPOSTER"], execute_imposter)

    interpreter = Interpreter([hello_world, read_back, imposter])
    interpreter.interpret_text("IMPOSTER")
