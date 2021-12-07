from .challenge import *

base_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_can_estimate_fuel():
    assert fuel_consumption(1, base_input) == 41
    assert fuel_consumption(2, base_input) == 37
    assert fuel_consumption(3, base_input) == 39
    assert fuel_consumption(10, base_input) == 71


def test_can_find_minimum():
    assert find_position(base_input) == 2


def test_can_estimate_triangular_fuel():
    assert triangular_fuel_consumption(5, base_input) == 168
    assert triangular_fuel_consumption(2, base_input) == 206


def test_can_find_triangular_minimum():
    assert find_triangular_position(base_input) == 5
