from typing import Generator
from time import sleep

from quackinter.config import Config


class Context:
    def __init__(self, ducky: list[str], config: Config) -> None:
        self._ducky_code = ducky
        self._current_line = 0
        self.config = config
        self._time_between_lines_override = config.interval
        self._default_delay = 0

    def get_line_gen(self) -> Generator[tuple[int, str]]:
        for index, line in enumerate(self._ducky_code):
            # Separated for readability
            yield (index, line)
            sleep(self.default_delay)
            self._current_line += 1

    def __iter__(self):
        return self.get_line_gen()

    def __next__(self):
        try:
            returnable = self._ducky_code[self.current_line_index]
        except IndexError:
            raise StopIteration("There are no more lines to iterate")
        self._current_line += 1
        return returnable

    @property
    def current_line_index(self):
        return self._current_line

    @property
    def current_line(self):
        return self._ducky_code[self._current_line]

    @property
    def default_delay(self):
        return self._time_between_lines_override or self._default_delay
    
    @default_delay.setter
    def default_delay(self, value: float):
        self._default_delay = value
        return value
    