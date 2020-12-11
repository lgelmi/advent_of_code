import unittest

from .day11 import *

free = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
full = """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""
left = """#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""
occupied = """#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"""
stable = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""


class TestDay11(unittest.TestCase):
    def test_from_str(self):
        self.assertEqual(
            [
                [True, None, True, True, None, False, True, None, True, True],
                [True, False, True, True, True, True, True, None, True, True],
            ],
            seats_from_string(
                """#.##.L#.##
#L#####.##"""
            ),
        )

    def test_to_str(self):
        self.assertEqual(
            """#.##.L#.##
#L#####.##""",
            seats_to_str(
                [
                    [True, None, True, True, None, False, True, None, True, True],
                    [True, False, True, True, True, True, True, None, True, True],
                ]
            ),
        )

    def test_fill(self):
        self.assertEqual(seats_from_string(full), fill_seats(seats_from_string(free)))

    def test_should_occupy(self):
        self.assertEqual(
            False,
            should_be_occupied(0, 1, [[None, False, True], [True, False, False]], 3, 2),
        )

    def test_occupy(self):
        self.assertEqual(
            seats_from_string(occupied), occupy_seats(seats_from_string(left))
        )

    def test_leave_seat(self):
        self.assertEqual(
            False,
            update_left_state(0, 1, [[None, True, True], [True, True, True]], 2, 3),
        )

    def test_leave(self):
        self.assertEqual(seats_from_string(left), leave_seats(seats_from_string(full)))

    def test_stability(self):
        self.assertEqual(
            seats_from_string(stable), find_stable_seats(seats_from_string(free))
        )

    def test_visible_occupied(self):
        self.assertEqual(
            0,
            visible_occupied(
                3,
                3,
                seats_from_string(
                    """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""
                ),
                7,
                7,
            ),
        )
        self.assertEqual(
            0,
            visible_occupied(
                1,
                0,
                seats_from_string(
                    """.............
.L.L.#.#.#.#.
............."""
                ),
                3,
                13,
            ),
        )
        self.assertEqual(
            8,
            visible_occupied(
                4,
                3,
                seats_from_string(
                    """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""
                ),
                9,
                9,
            ),
        )

    def test_occupy_visible(self):
        self.assertEqual(
            seats_from_string(
                """#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#"""
            ),
            occupy_visible_seats(
                seats_from_string(
                    """#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""
                )
            ),
        )

    def test_leave_visible(self):
        self.assertEqual(
            seats_from_string(
                """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""
            ),
            leave_visible_seats(
                seats_from_string(
                    """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""
                )
            ),
        )
