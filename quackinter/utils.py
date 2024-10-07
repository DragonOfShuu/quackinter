def separate_cmd(string: str) -> list[str]:
    separate = string.split(" ", 1)
    return [separate[0].upper(), separate[1]]
