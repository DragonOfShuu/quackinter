
class Context:
    def __init__(self, ducky: list[str]) -> None:
        self._ducky_code = ducky
        self._current_line = 0

    def get_line_gen(self):
        for index,line in enumerate(self._ducky_code):
            # Separated for readability
            yield [index, line]
            self._current_line+=1

    def __iter__(self):
        return self.get_line_gen()
    
    def __next__(self):
        try:
            returnable = self._ducky_code[self.current_line_index]
        except IndexError:
            raise StopIteration("There are no more lines to iterate")
        self._current_line+=1
        return returnable

    @property
    def current_line_index(self):
        return self._current_line
    
    @property
    def current_line(self):
        return self._ducky_code[self._current_line]
    