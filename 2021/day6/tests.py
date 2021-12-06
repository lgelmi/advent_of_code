from .challenge import *

base_input = [3, 4, 3, 1, 2]


def test_can_simulate():
    assert simulate_growth(base_input, 18) == 26
    assert simulate_growth(base_input, 80) == 5934


def test_can_fornicate():
    fornicator = Fornicator9000(base_input)
    day1 = fornicator.fornicate()
    assert sum(day1.values()) == 5
    day2 = day1.fornicate()
    assert sum(day2.values()) == 6
