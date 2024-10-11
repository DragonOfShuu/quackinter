from quackinter.commands.command import Command
from quackinter.context import Context
from quackinter.key_injector import KeyInjector


class ModifierKey(Command):
    conversion_chart = {
        "CTRL": ["CTRL"],
        "CONTROL": ["CTRL"],
        "SHIFT": ["SHIFT"],
        "ALT": ["ALT"],
        "WIN": ["WIN"],
        "CTRL-SHIFT": ["CTRL", "SHIFT"],
        "CTRL-ALT": ["CTRL", "ALT"],
        "ALT-SHIFT": ["ALT", "SHIFT"],
        "ALT-WIN": ["ALT", "WIN"],
        "WIN-SHIFT": ["WIN", "SHIFT"],
        "WIN-CTRL": ["WIN", "CTRL"],
        "APP": ["APPS"],
        "MENU": ["APPS"],
    }
    names = conversion_chart.keys()

    @staticmethod
    def _normalize_cmd(cmd: str):
        return cmd.replace('+', '-').replace('GUI', 'WIN').replace('WINDOWS', 'WIN')
        
    @classmethod
    def is_this_command(cls, name: str, data: str) -> bool:
        return cls._normalize_cmd(name) in cls.conversion_chart.keys()

    @classmethod
    def execute(cls, context: Context, cmd: str, data: str) -> None:
        norm_cmd = cls._normalize_cmd(cmd)
        key_injector = KeyInjector(context)
        key_injector.hotkey([*norm_cmd.split('-'), *data.strip().split(' ')])

