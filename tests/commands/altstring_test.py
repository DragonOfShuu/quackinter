from quackinter import AltStringCommand


def test_convert_char():
    test_char = AltStringCommand.convert_char("™")
    assert test_char == "0153"
    test_char = AltStringCommand.convert_char("ñ")
    assert test_char == "164"
    test_char = AltStringCommand.convert_char("{")
    assert test_char == "123"
    test_char = AltStringCommand.convert_char("}")
    assert test_char == "125"
    test_char = AltStringCommand.convert_char("h")
    assert test_char == "104"
    test_char = AltStringCommand.convert_char("e")
    assert test_char == "101"


def test_convert_test():
    test_text = AltStringCommand.convert_text("hello world")
    assert test_text == [
        "104",
        "101",
        "108",
        "108",
        "111",
        "32",
        "119",
        "111",
        "114",
        "108",
        "100",
    ]
