import copy
import itertools
from pathlib import Path
from typing import List, Tuple

steps = tuple(itertools.product((0, -1, 1), (0, -1, 1), (0, -1, 1)))[1:]


class Period(list):
    def __getitem__(self, idx):
        return super().__getitem__(idx % len(self))


Layer = Period[Period[bool]]
Space = Period[Layer]


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def make_empty_layer(width: int, height: int) -> Layer:
    return Period(Period(False for _ in range(height)) for _ in range(width))


def get_nearest(z: int, x: int, y: int, space: Space) -> List[int]:
    return [((z + dz, x + dx, y + dy), space[z + dz][x + dx][y + dy]) for dx, dy, dz in steps]


def initialize_cycle(space: Space) -> Tuple[Space, Space]:
    width, height = len(space[0]), len(space[0][0])
    start = copy.deepcopy(space)
    start.insert(0, make_empty_layer(width, height))
    start.append(make_empty_layer(width, height))
    end = copy.deepcopy(start)
    return start, end


def get_new_state(z, x, y, space: Space) -> bool:
    current = space[z][x][y]
    nearest = get_nearest(z, x, y, space)
    active = sum(nearest)
    return (active in (2, 3)) if current else active == 3


def conway_cycle(space: Space) -> Space:
    start, end = initialize_cycle(space)
    length, width, height = len(start), len(start[0]), len(start[0][0])
    for z, x, y in itertools.product(range(length), range(width), range(height)):
        end[z][x][y] = get_new_state(z, y, x, start)
    return end


def parse_values(content: str) -> Space:
    return Period(
        [Period(Period(col == "#" for col in row) for row in content.split())]
    )


def solve_1(values):
    print("--------------- 1 ---------------")
    print(*conway_cycle(values), sep="\n")


def solve_2(values):
    print("--------------- 2 ---------------")


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
