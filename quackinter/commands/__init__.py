from quackinter.commands.command import Command

from quackinter.commands.altchar import AltCharCommand
from quackinter.commands.default_delay import DefaultDelayCommand
from quackinter.commands.delay import DelayCommand
from quackinter.commands.general_key import GeneralKeyCommand
from quackinter.commands.hold_release import HoldReleaseCommand
from quackinter.commands.media import MediaCommand
from quackinter.commands.rem import RemCommand
from quackinter.commands.repeat import RepeatCommand
from quackinter.commands.string import StringCommand
from quackinter.commands.stringln import StringLnCommand
from quackinter.commands.sysrq import SysRqCommand
from quackinter.commands.wait_for_button_press import WaitForButtonPressCommand

command_list: list[type[Command]] = [
    AltCharCommand,
    DefaultDelayCommand,
    DelayCommand,
    GeneralKeyCommand,
    HoldReleaseCommand,
    MediaCommand,
    RemCommand,
    RepeatCommand,
    StringCommand,
    StringLnCommand,
    SysRqCommand,
    WaitForButtonPressCommand,
]
