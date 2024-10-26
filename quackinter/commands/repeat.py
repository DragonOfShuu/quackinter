from quackinter.commands.command import Command
from quackinter.errors import InterpretationSyntaxError
from quackinter.stack_context import StackContext


class RepeatCommand(Command):
    names = ["REPEAT"]

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        line = context.get_line_offset(1)
        if line is None:
            raise InterpretationSyntaxError("There must be a line before repeat to run")

        new_stack = context.stack.new_stack()
        new_stack.run([line.line])
