from quackinter.commands.command import Command
from quackinter.config import Config
from quackinter.environment import Environment
from quackinter.stack_context import StackContext

import pyautogui as pyag

class HoldReleaseCommand(Command):
    HELD_KEYS_KEY = "HELD_KEYS"
    names = ["RELEASE", "HOLD"]

    @classmethod
    def _get_keys(cls, environment: Environment) -> list[str]:
        return environment.global_vars[cls.HELD_KEYS_KEY]

    @classmethod
    def global_environment_init(cls, environment: Environment, config: Config) -> None:
        environment.global_vars[cls.HELD_KEYS_KEY] = []

    @classmethod
    def global_environment_exit(cls, environment: Environment, config: Config) -> None:
        keys: list[str] = cls._get_keys(environment)
        cls._release_keys(environment, keys)

    @classmethod
    def _release_keys(cls, environment: Environment, to_release: list[str]):
        keys: list[str] = cls._get_keys(environment)
        for key in to_release:
            pyag.keyUp(key)
            keys.remove(key)

    @classmethod
    def _hold_keys(cls, environment: Environment, to_hold: list[str]):
        keys = cls._get_keys(environment)
        for key in to_hold:
            pyag.keyDown(key)
            keys.append(key)

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        command = cmd.upper()
        keys = [key for key in data.strip().split(' ') if key.strip()]

        if command == "HOLD":
            cls._hold_keys(context.environment, keys)
        else:
            cls._release_keys(context.environment, keys)
