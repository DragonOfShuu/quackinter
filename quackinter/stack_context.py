from __future__ import annotations

from typing import Generator
from time import sleep

from quackinter.config import Config
from quackinter.environment import Environment


class StackContext:
    def __init__(
        self, ducky: list[str], config: Config, old_context: StackContext | None = None
    ) -> None:
        self._ducky_code = ducky
        self._current_line = 0
        self.config = config
        self._time_between_lines_override = config.interval
        self._time_between_chars_override = config.char_interval

        if old_context:
            self.environment = old_context.environment.extend()
        else:
            self.environment = Environment()

    def get_line_gen(self) -> Generator[tuple[int, str]]:
        for index, line in enumerate(self._ducky_code):
            # Separated for readability
            yield (index, line)
            sleep(self.environment.global_vars["_DEFAULT_DELAY"])
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
