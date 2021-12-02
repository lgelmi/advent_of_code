from .challenge import *


def test_base():
    assert (
        navigate_submarine(
            [
                ("forward", 5),
                ("down", 5),
                ("forward", 8),
                ("up", 3),
                ("down", 8),
                ("forward", 2),
            ]
        )
        == SubMarine(15, 10)
    )
