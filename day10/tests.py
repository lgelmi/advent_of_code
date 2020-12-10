import unittest

from .day10 import *

short = sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
long = sorted(
    [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
)


class TestDay10(unittest.TestCase):
    def test_steps(self):
        self.assertEqual(
            [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3],
            jolt_steps(short),
        )

    def test_difference(self):
        self.assertEqual(
            35,
            jolt_difference(short),
        )

    def test_starts(self):
        self.assertEqual(1, get_combination_count(1))
        self.assertEqual(2, get_combination_count(2))
        self.assertEqual(4, get_combination_count(3))
        self.assertEqual(7, get_combination_count(4))
        self.assertEqual(13, get_combination_count(5))

    def test_counter(self):
        self.assertEqual(
            8, count_combination(sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]))
        )
        self.assertEqual(
            19208,
            count_combination(long),
        )
