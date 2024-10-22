from quackinter.commands.command import Command

from quackinter.commands.default_delay import DefaultDelay
from quackinter.commands.delay import Delay
from quackinter.commands.general_key import GeneralKey
from quackinter.commands.rem import Rem
from quackinter.commands.string import String
from quackinter.commands.stringln import StringLn
from quackinter.commands.sysrq import SysRq
from quackinter.commands.wait_for_button_press import WaitForButtonPress

command_list: list[type[Command]] = [
    DefaultDelay,
    Delay,
    GeneralKey,
    Rem,
    String,
    StringLn,
    SysRq,
    WaitForButtonPress,
]
