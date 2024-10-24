from quackinter.commands.command import Command

from quackinter.commands.default_delay import DefaultDelayCommand
from quackinter.commands.delay import DelayCommand
from quackinter.commands.general_key import GeneralKeyCommand
from quackinter.commands.rem import RemCommand
from quackinter.commands.string import StringCommand
from quackinter.commands.stringln import StringLnCommand
from quackinter.commands.sysrq import SysRqCommand
from quackinter.commands.wait_for_button_press import WaitForButtonPressCommand

command_list: list[type[Command]] = [
    DefaultDelayCommand,
    DelayCommand,
    GeneralKeyCommand,
    RemCommand,
    StringCommand,
    StringLnCommand,
    SysRqCommand,
    WaitForButtonPressCommand,
]
