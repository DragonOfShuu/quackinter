from quackinter.commands.command import Command
from quackinter.errors import InvalidArgError, UnsupportedError
from quackinter.stack_context import StackContext
from quackinter.key_injector import KeyInjector

from typing import Literal, get_args, cast
import screen_brightness_control as sbc
import platform as pf
import subprocess

MediaArgType = Literal[
    # Machine Commands
    "POWER",
    "REBOOT",
    "SLEEP",
    "LOGOFF",
    "VOLUME_UP",
    "VOLUME_DOWN",
    "BRIGHT_UP",
    "BRIGHT_DOWN",
    # Keys
    "HOME",
    "BACK",
    "FORWARD",
    "REFRESH",
    "SNAPSHOT",
    # Media
    "PLAY",
    "PAUSE",
    "PLAY_PAUSE",
    "NEXT_TRACK",
    "PREV_TRACK",
    "STOP",
    "MUTE",
    # Mac
    "FN",
    # Misc
    "EJECT",
    "EXIT",
]


class MediaCommand(Command):
    subcommands = list(get_args(MediaArgType))

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        clean_data: MediaArgType = cast(MediaArgType, data.strip().upper())
        if clean_data not in cls.subcommands:
            raise InvalidArgError(
                f'"{data.strip()}" is not an acceptible arg. Accepted args for MEDIA: {', '.join(cls.subcommands)}'
            )

        media_argument = MediaArgument(context)
        media_method = getattr(MediaArgument, clean_data.lower())
        media_method(media_argument)


class MediaArgument:
    def __init__(self, context: StackContext):
        self.is_windows = pf.uname()[0] == "Windows"
        self.is_mac = pf.uname()[0] == "Darwin"
        self.is_linux = pf.uname()[0] == "Linux"
        self.key_injector = KeyInjector(context)

    def power(self):
        if self.is_windows:
            subprocess.run(["shutdown", "/s", "/t 0"])
        else:
            subprocess.run(["shutdown", "now"])

    def reboot(self):
        if self.is_windows:
            subprocess.run(["shutdown", "/r", "/t 0"])
        else:
            subprocess.run(["reboot"])

    def sleep(self):
        self.key_injector.press("sleep")

    def logoff(self):
        if self.is_windows:
            subprocess.run(["shutdown", "/l", "/t 0"])
        else:
            raise UnsupportedError(
                "Logoff is not supported for unix operating systems."
            )

    def volume_up(self):
        self.key_injector.press("volumeup")

    def volume_down(self):
        self.key_injector.press("volumedown")

    def bright_up(self):
        current_brightness = sbc.get_brightness()
        sbc.set_brightness(min(100, current_brightness + 5))

    def bright_down(self):
        current_brightness = sbc.get_brightness()
        sbc.set_brightness(min(100, current_brightness + 5))

    def home(self):
        self.key_injector.press("browserhome")

    def back(self):
        self.key_injector.press("browserback")

    def forward(self):
        self.key_injector.press("browserforward")

    def refresh(self):
        if self.is_mac:
            self.key_injector.hotkey(["command", "r"])
        else:
            self.key_injector.hotkey(["ctrl", "r"])

    def snapshot(self):
        raise UnsupportedError("Snapshot key is unsupported.")

    def play(self):
        self.key_injector.press("play")

    def pause(self):
        self.key_injector.press("pause")

    def play_pause(self):
        self.key_injector.press("playpause")

    def next_track(self):
        self.key_injector.press("nexttrack")

    def prev_track(self):
        self.key_injector.press("prevtrack")

    def stop(self):
        self.key_injector.press("stop")

    def mute(self):
        self.key_injector.press("volumemute")

    def fn(self):
        self.key_injector.press("fn")

    def eject(self):
        raise UnsupportedError("Eject key is unsupported.")

    def exit(self):
        raise UnsupportedError("Exit key is unsupported.")
