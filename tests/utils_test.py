import pytest

from quackinter.utils import extract_cmd


def test_extract_cmd():
    cmd, data = extract_cmd("stringln THIS IS DATA")
    assert cmd == "STRINGLN"
    assert data == "THIS IS DATA"


def test_extract_cmd_empty_string():
    """
    extract_cmd should error when
    there is an empty string
    """

    with pytest.raises(ValueError):
        extract_cmd("")
