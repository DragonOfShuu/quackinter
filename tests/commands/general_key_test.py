from quackinter import GeneralKeyCommand

def test_normalize_cmd():
    assert GeneralKeyCommand._normalize_cmd("CONTROL+ALT+DELETE") == ["ctrl", "alt", "delete"]
    assert GeneralKeyCommand._normalize_cmd("WINDOWS+E") == ["win", "E"]
    assert GeneralKeyCommand._normalize_cmd("APP+MENU") == ["apps", "apps"]

def test_is_this_command():
    assert GeneralKeyCommand.is_this_command("WIN", "")
    # test a bit of capitalization
    assert GeneralKeyCommand.is_this_command("win", "")
    assert GeneralKeyCommand.is_this_command("CONTROL+ALT+DELETE", "")
    # test a bit of capitalization
    assert GeneralKeyCommand.is_this_command("control+alt+delete", "")
    assert GeneralKeyCommand.is_this_command("WINDOWS+E", "")
    assert not GeneralKeyCommand.is_this_command("UNKNOWN+COMMAND", "")
