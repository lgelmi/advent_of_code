import unittest

from .day9 import *


class TestDay9(unittest.TestCase):
    def test_first_missing(self):
        self.assertEqual(
            127,
            first_missing(
                [
                    35,
                    20,
                    15,
                    25,
                    47,
                    40,
                    62,
                    55,
                    65,
                    95,
                    102,
                    117,
                    150,
                    182,
                    127,
                    219,
                    299,
                    277,
                    309,
                    576,
                ],
                5,
            ),
        )

    def test_couple_sum(self):
        self.assertEqual(
            [15, 25, 47, 40],
            get_consecutive(
                [
                    35,
                    20,
                    15,
                    25,
                    47,
                    40,
                    62,
                    55,
                    65,
                    95,
                    102,
                    117,
                    150,
                    182,
                    127,
                    219,
                    299,
                    277,
                    309,
                    576,
                ],
                127,
            ),
        )
