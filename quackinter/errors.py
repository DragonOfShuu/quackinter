from quackinter.context import Context


class QuackinterError(Exception):
    pass


class OutsideContextError(QuackinterError):
    pass


class InterpretationError(QuackinterError):
    def __init__(self, *args: object):
        super().__init__(*args)
        self.contexts = []
    
    def add_context(self, new_context: Context):
        self.contexts.append(new_context)


class CommandNotDefinedError(InterpretationError):
    pass


class NotANumberError(InterpretationError):
    pass