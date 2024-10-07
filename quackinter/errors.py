from quackinter.context import Context


class QuackinterError(Exception):
    pass


class InterpretationError(QuackinterError):
    def __init__(self, line: int, context: Context, *args: object):
        super().__init__(*args)
        self.line = line
        self.context = context


class CommandNotDefinedError(InterpretationError):
    pass
