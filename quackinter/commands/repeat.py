from quackinter.commands.command import Command
from quackinter.errors import InterpretationSyntaxError
from quackinter.stack import Stack


class RepeatCommand(Command):
    names = ["REPEAT"]

    def execute(self, stack: Stack, cmd: str, data: str) -> None:
        line = stack.context.get_line_offset(1)
        if line is None:
            raise InterpretationSyntaxError("There must be a line before repeat to run")

        new_stack = stack.new_stack()
        new_stack.run([line.line])
