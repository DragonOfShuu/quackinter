class Sanitizer:
    @staticmethod
    def sanitize_lines(text: list[str]):
        return [line.lstrip() for line in text if line]
