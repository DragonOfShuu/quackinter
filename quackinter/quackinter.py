from quackinter.config import Config
from quackinter.interpreter import Interpreter


def interpret(ducky: str, config: Config):
    interpreter = Interpreter(config=config)
    interpreter.interpret_text(ducky)
