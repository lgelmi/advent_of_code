from numpy.testing import assert_array_equal

from .challenge import *

base_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

base_octopussies = parse_input(base_input)


def test_can_charge():
    octopussies = copy.deepcopy(base_octopussies)
    expected = parse_input(
        """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""
    )
    charge(octopussies)
    assert_array_equal(octopussies, expected)


def test_can_find_flashes():
    octopussies = copy.deepcopy(base_octopussies)
    assert find_flashes(octopussies) == 1656


def test_can_find_sync():
    octopussies = copy.deepcopy(base_octopussies)
    assert find_sync(octopussies) == 195
