import unittest

from .day12 import *


class TestDay12(unittest.TestCase):
    def test_direction(self):
        self.assertEqual(
            Ship(Position(17, -8), Direction.South),
            follow_directions(
                parse_values(
                    """F10
N3
F7
R90
F11"""
                )
            ),
        )

    def test_manhattan(self):
        self.assertEqual(
            25,
            Ship().execute_commands(
                parse_values(
                    """F10
N3
F7
R90
F11"""
                )
            ).position.manhattan,
        )

    def test_waypoint_forward(self):
        self.assertEqual(
            WaypointShip(Position(100, 10), Position(10, 1)),
            WaypointShip().move_to_waypoint(10),
        )
        self.assertEqual(
            WaypointShip(Position(170, 38), Position(10, 4)),
            WaypointShip(Position(100, 10), Position(10, 4)).move_to_waypoint(7),
        )

    def test_waypoint_north(self):
        self.assertEqual(
            WaypointShip(Position(100, 10), Position(10, 4)),
            WaypointShip(Position(100, 10), Position(10, 1)).move_waypoint_north(3),
        )

    def test_rotate_waypoint(self):
        self.assertEqual(
            WaypointShip(Position(170, 38), Position(4, -10)),
            WaypointShip(Position(170, 38), Position(10, 4)).rotate_waypoint_right(90),
        )