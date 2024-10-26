from __future__ import annotations

from typing import Generator
from time import sleep

from quackinter.environment import Environment
from quackinter.errors import QuackinterError
from quackinter.line import Line
from quackinter.sanitizer import Sanitizer
from quackinter.stack import Stack


class StackContext:
    def __init__(
        self, ducky: list[str], environment: Environment, stack: Stack
    ) -> None:
        self._ducky_code = ducky
        self.stack = stack
        self.config = environment.config
        self._time_between_lines_override = self.config.interval
        self._time_between_chars_override = self.config.char_interval

        self._current_line: Line|None = None
        self.is_running = False
        self.generated_lines: list[Line] = []

        self.environment = environment

    def get_line_gen(self) -> Generator[Line]:
        if self.is_running:
            raise QuackinterError("StackContext is still running, cannot run a new instance.")

        self.is_running = True
        self.generated_lines = []
        for index, line in enumerate(self._ducky_code):
            if not line.strip(): 
                continue
            
            new_line = Line(self._sanitize_line(line), index, line)
            self.generated_lines.append(new_line)
            self._current_line = new_line
            yield new_line
            sleep(self.environment.global_vars["_DEFAULT_DELAY"])
        self.is_running = False
        self._current_line = None

    def _sanitize_line(self, line: str) -> str:
        return Sanitizer.santize_str(line)

    def get_line_offset(self, count: int):
        """
        Get a line from $count lines ago. Enter `1` to
        get the previous line from this one, `0` to get
        this line.
        """
        if not self.is_running: 
            raise QuackinterError("To get previous lines, StackContext must be running.")
        curr_ind = len(self.generated_lines) - 1
        new_ind = curr_ind - count
        if new_ind < 0 or new_ind > curr_ind:
            return None
        return self.generated_lines[new_ind]
        

    def __iter__(self):
        return self.get_line_gen()

    @property
    def current_line_index(self):
        if not self.is_running or not self._current_line:
            raise QuackinterError("To get the current line index, StackContext must be running.")
        return self._current_line.line_index

    @property
    def current_line(self):
        return self._current_line
