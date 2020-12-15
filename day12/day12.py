import dataclasses
import enum
import functools
from pathlib import Path
from typing import List


class Direction(enum.Enum):
    North = "N"
    South = "S"
    West = "W"
    East = "E"

    def rotate(self, degree: int) -> "Direction":
        order = [Direction.East, Direction.North, Direction.West, Direction.South]
        current = order.index(self)
        return order[(current + degree // 90) % 4]


@dataclasses.dataclass
class Position:
    east: int
    north: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.east + other.east, self.north + other.north)

    def __mul__(self, other: int) -> "Position":
        return Position(other * self.east, other * self.north)

    def rotate(self, degree: int) -> "Position":
        amount = (degree // 90) % 4
        if not amount:
            return self

        if amount == 1:
            return Position(-self.north, self.east)

        if amount == 2:
            return Position(-self.east, -self.north)

        if amount == 3:
            return Position(self.north, -self.east)

    @property
    def manhattan(self) -> int:
        return abs(self.east) + abs(self.north)


@dataclasses.dataclass
class Ship:
    position: Position = Position(0, 0)
    direction: Direction = Direction.East

    def execute_commands(self, commands: List[str]) -> "Ship":
        mapping = {
            "N": Ship.move_north,
            "S": Ship.move_south,
            "E": Ship.move_east,
            "W": Ship.move_west,
            "L": Ship.rotate_left,
            "R": Ship.rotate_right,
            "F": Ship.move_front,
        }

        return functools.reduce(
            lambda ship, direction: direction[0](ship, direction[1]),
            [(mapping[command[0]], int(command[1:])) for command in commands],
            self,
        )

    def move_front(self, amount: int):
        directions = {
            Direction.East: self.move_east,
            Direction.North: self.move_north,
            Direction.South: self.move_south,
            Direction.West: self.move_west,
        }
        # noinspection PyArgumentList
        return directions[self.direction](amount)

    def move_south(self, amount: int):
        return self.move_north(-amount)

    def move_north(self, amount: int):
        return self.move(Position(0, amount))

    def move_west(self, amount: int):
        return self.move_east(-amount)

    def move_east(self, amount: int):
        return self.move(Position(amount, 0))

    def move(self, movement: Position) -> "Ship":
        return Ship(self.position + movement, self.direction)

    def rotate_right(self, amount: int) -> "Ship":
        return self.rotate_left(-amount)

    def rotate_left(self, amount: int) -> "Ship":
        return Ship(self.position, self.direction.rotate(amount))


@dataclasses.dataclass
class WaypointShip:
    position: Position = Position(0, 0)
    waypoint: Position = Position(10, 1)

    def execute_commands(self, commands: List[str]) -> "WaypointShip":
        mapping = {
            "N": WaypointShip.move_waypoint_north,
            "S": WaypointShip.move_waypoint_south,
            "E": WaypointShip.move_waypoint_east,
            "W": WaypointShip.move_waypoint_west,
            "L": WaypointShip.rotate_waypoint_left,
            "R": WaypointShip.rotate_waypoint_right,
            "F": WaypointShip.move_to_waypoint,
        }

        return functools.reduce(
            lambda ship, direction: direction[0](ship, direction[1]),
            [(mapping[command[0]], int(command[1:])) for command in commands],
            self,
        )

    def move_to_waypoint(self, amount: int) -> "WaypointShip":
        return WaypointShip(self.position + self.waypoint * amount, self.waypoint)

    def move_waypoint_south(self, amount: int) -> "WaypointShip":
        return self.move_waypoint_north(-amount)

    def move_waypoint_north(self, amount: int) -> "WaypointShip":
        return self.move_waypoint(Position(0, amount))

    def move_waypoint_west(self, amount: int) -> "WaypointShip":
        return self.move_waypoint_east(-amount)

    def move_waypoint_east(self, amount: int) -> "WaypointShip":
        return self.move_waypoint(Position(amount, 0))

    def move_waypoint(self, movement: Position) -> "WaypointShip":
        return WaypointShip(self.position, self.waypoint + movement)

    def rotate_waypoint_right(self, amount: int) -> "WaypointShip":
        return self.rotate_waypoint_left(-amount)

    def rotate_waypoint_left(self, amount: int) -> "WaypointShip":
        return WaypointShip(self.position, self.waypoint.rotate(amount))


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> List[str]:
    return content.split()


def solve_1(values):
    print("--------------- 1 ---------------")
    ship = Ship().execute_commands(values)
    print(ship)
    print(ship.position.manhattan)


def solve_2(values):
    print("--------------- 2 ---------------")
    ship = WaypointShip().execute_commands(values)
    print(ship)
    print(ship.position.manhattan)


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
