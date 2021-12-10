from .challenge import *

base_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]
base_heightmap = get_array(base_input)


def test_can_find_minimums():
    assert get_minimums(base_heightmap) == [1, 0, 5, 5]


def test_can_recognize_minimum():
    assert is_minimum(base_heightmap, 0, 1, 5, 10)
    assert is_minimum(base_heightmap, 0, 9, 5, 10)
    assert not is_minimum(base_heightmap, 0, 5, 5, 10)


def test_can_evaluate_sum():
    assert sum_minimums(base_heightmap) == 15

def test_can_get_basin_size():
    assert get_basin_size(base_heightmap, 0, 1, 5, 10) == 3
    assert get_basin_size(base_heightmap, 0, 9, 5, 10) == 9
    assert get_basin_size(base_heightmap, 2, 2, 5, 10) == 14
    assert get_basin_size(base_heightmap, 4, 6, 5, 10) == 9
