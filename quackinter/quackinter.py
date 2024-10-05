from quackinter.stack import Stack

def interpret(ducky: str, delay: float|None = None):
    new_ducky = ducky.split('\n')

    stack = Stack(new_ducky)
    stack.run()