from quackinter.config import Config
from quackinter.environment import Environment
from quackinter.errors import VariableNotDefinedError

import pytest


def test_scope():
    global_env = Environment.create_global([], Config())
    local_env = global_env.extend()

    global_env.add_var("GLOBAL_ONLY", True)
    local_env.add_var("LOCAL_ONLY", True)

    assert global_env.get_var(
        "GLOBAL_ONLY"
    ), "Global variable should be true when getting from global"
    assert local_env.get_var(
        "LOCAL_ONLY"
    ), "Local variable should be true when getting from local"
    assert local_env.get_var(
        "GLOBAL_ONLY"
    ), "Global variable should be true when getting from local"

    with pytest.raises(VariableNotDefinedError):
        assert (
            global_env.get_var("LOCAL_ONLY") is None
        ), "Local only variable should be unreachable from the global scope"
