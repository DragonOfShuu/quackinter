from quackinter.commands.command import Command
from quackinter.stack import Stack
from tests.testing_tools.make_command import make_command

def hello_world_cmd(global_list: list[str]):
    def execute(command_self: Command, stack: Stack, cmd: str, data: str):
        global_list.append("Hello World")

    return make_command(["HELLO_WORLD"], execute)