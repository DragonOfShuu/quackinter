import typing
from quackinter.context import Context

import pyautogui as pyag

from quackinter.errors import KeyNotExistError

AcceptedKeysType = typing.Literal['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

accepted_keys = typing.get_args(AcceptedKeysType)

class KeyInjector:
    ACCEPTED_KEYS = accepted_keys

    def __init__(self, context: Context):
        self.context = context
    
    def is_key(self, key: str):
        return key.lower() in self.ACCEPTED_KEYS
    
    def _verify_key(self, key: str):
        if not self.is_key(key):
            raise KeyNotExistError(f'{key} is not a valid key.')
        return key
    
    def press(self, key: str):
        pyag.press(self._verify_key(key), interval=self.context.config.char_interval)
    
    def write(self, text: str):
        pyag.write(text, interval=self.context.config.char_interval)
    
    def hotkey(self, hotkeys: list[str]):
        keys = [(key.lower() if len(key) > 1 else key) for key in hotkeys if key]
        for key in keys:
            self._verify_key(key)
        pyag.hotkey(*keys, interval=self.context.config.char_interval)

    def hold(self, key: str|list[str]):
        new_key = [key] if isinstance(key, str) else key
        return pyag.hold([self._verify_key(key) for key in new_key if key])