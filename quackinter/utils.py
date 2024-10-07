def extract_cmd(string: str) -> tuple[str, str]:
    separate = string.split(" ", 1)
    return (separate[0].upper(), separate[1])
