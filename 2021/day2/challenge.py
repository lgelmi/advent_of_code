import dataclasses
from pathlib import Path
from typing import List, Tuple


InputType = List[Tuple[str, int]]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return [
            (direction, int(amount))
            for direction, amount in map(lambda row: row.split(), f.read().split("\n"))
        ]


def solve_1(values: InputType):
    submarine = navigate_submarine(SubMarine(0,0), values)
    print(submarine.position * submarine.depth)


@dataclasses.dataclass
class SubMarine:
    position: int
    depth: int

    def move(self, direction: str, amount: int):
        match direction:
            case "up":
                self.depth -= amount
            case "forward":
                self.position += amount
            case "down":
                self.depth += amount


def navigate_submarine(submarine: SubMarine, directions: InputType) -> SubMarine:
    for direction, amount in directions:
        submarine.move(direction, amount)
    return submarine


def solve_2(values: InputType):
    submarine = navigate_submarine(AimedSubMarine(0,0, 0), values)
    print(submarine.position * submarine.depth)

@dataclasses.dataclass
class AimedSubMarine(SubMarine):
    aim: int

    def move(self, direction: str, amount: int):
        match direction:
            case "up":
                self.aim -= amount
            case "forward":
                self.position += amount
                self.depth += amount * self.aim
            case "down":
                self.aim += amount


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
