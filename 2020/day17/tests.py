import unittest

from .day17 import *

start = Period(
    [
        Period(
            [
                Period([False, True, False]),
                Period([False, False, True]),
                Period([True, True, True]),
            ]
        )
    ]
)

to_first = Period(
    [
        make_empty_layer(3, 3),
        Period(
            [
                Period([False, True, False]),
                Period([False, False, True]),
                Period([True, True, True]),
            ]
        ),
        make_empty_layer(3, 3),
    ]
)


first = Period(
    [
        Period(
            [
                Period([True, False, False]),
                Period([False, False, True]),
                Period([False, True, False]),
            ]
        ),
        Period(
            [
                Period([True, False, True]),
                Period([False, True, True]),
                Period([False, True, False]),
            ]
        ),
        Period(
            [
                Period([True, False, False]),
                Period([False, False, True]),
                Period([False, True, False]),
            ]
        ),
    ]
)


class TestDay17(unittest.TestCase):
    def test_neighbors(self):
        print(*get_nearest(0,0,0, to_first), sep="\n")
        # self.assertEqual([], get_nearest(1, 1, 1, to_first))

    def test_cycle(self):
        self.assertEqual(first, conway_cycle(start))
