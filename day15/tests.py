import unittest

from .day15 import *


class TestDay15(unittest.TestCase):
    def test_simple(self):
        simple = [0, 3, 6]
        self.assertEqual(0, play_memory(simple, 10))
        self.assertEqual(436, play_memory(simple, 2020))

    def test_others(self):
        self.assertEqual(1, play_memory([1, 3, 2], 2020))
