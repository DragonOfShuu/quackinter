from quackinter.commands.command import Command
from quackinter.context import Context


class DefaultDelay(Command):
    names = ["DEFAULT_DELAY", "DEFAULTDELAY"]

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        new_value = cls.convert_float(data.strip())
        context.default_delay = new_value
