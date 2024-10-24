from quackinter.commands.command import Command
from quackinter.config import Config
from quackinter.environment import Environment
from quackinter.stack_context import StackContext


class DefaultDelayCommand(Command):
    names = ["DEFAULT_DELAY", "DEFAULTDELAY"]
    GLOBAL_ENV_NAME = "_DEFAULT_DELAY"
    GLOBAL_ENV_OVERRIDE_NAME = "_DEFAULT_DELAY_OVERIDDEN"

    @classmethod
    def execute(cls, context: StackContext, cmd: str, data: str) -> None:
        # If the config was set, then any changes shall be overridden
        if context.environment.global_vars[cls.GLOBAL_ENV_OVERRIDE_NAME]:
            return
        new_value = cls.convert_float(data.strip())
        context.environment.global_vars[cls.GLOBAL_ENV_NAME] = new_value

    @classmethod
    def global_environment_init(cls, environment: Environment, config: Config) -> None:
        environment.global_vars[cls.GLOBAL_ENV_NAME] = config.interval or 0
        environment.global_vars[cls.GLOBAL_ENV_OVERRIDE_NAME] = (
            config.interval is not None
        )
