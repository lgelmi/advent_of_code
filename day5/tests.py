import unittest

from .day5 import *


class TestDay4(unittest.TestCase):
    def test_decode_row(self):
        self.assertEqual(44, decode_row("FBFBBFFRLR"))

    def test_decode_column(self):
        self.assertEqual(5, decode_column("FBFBBFFRLR"))

    def test_decode_seat_id(self):
        self.assertEqual(357, decode_seat_id("FBFBBFFRLR"))

    def test_decode_seats(self):
        self.assertEqual(
            [567, 119, 820],
            [decode_seat_id(seat) for seat in ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]],
        )

    def test_highest(self):
        self.assertEqual(
            820,
            highest_pass(["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]),
        )
