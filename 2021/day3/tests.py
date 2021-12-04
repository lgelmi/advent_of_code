from .challenge import *
from numpy.testing import assert_array_equal

base_input = numpy.array(
    [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
    ]
)


def test_can_convert_to_decimal():
    assert bin_list_to_dec([1, 0, 1, 1, 0]) == 22


def test_most_common():
    assert get_most_commons(base_input) == [1, 0, 1, 1, 0]


def test_power_consumption():
    assert get_power_consumption(base_input) == 198

def test_life_support():
    assert get_life_support_rating(base_input) == 230


def test_filter():
    assert_array_equal(
        filter_rows(base_input[:4], lambda row: row == 1, 0), base_input[1:4]
    )
