import copy
from dataclasses import dataclass
from pathlib import Path
from queue import SimpleQueue
from typing import List, Set, Tuple

import numpy
from numpy.typing import NDArray

CHARGE_LIMIT = 9


@dataclass
class Octopussy:
    flashed: bool = False
    charge: int = 0

    def init_next_step(self):
        if self.flashed:
            self.charge = 0
        self.flashed = False

    def charge_and_flash(self) -> bool:
        if self.flashed:
            return False

        self.charge += 1

        if self.charge > CHARGE_LIMIT:
            self.flashed = True
            return True

        return False

    def has_flashed(self) -> bool:
        return self.flashed


InputType = NDArray[Octopussy]


# noinspection DuplicatedCode
def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_input(f.read())


def parse_input(content: str) -> InputType:
    return numpy.array(list(map(parse_row, content.split("\n"))))


def parse_row(row: str) -> List[Octopussy]:
    return [Octopussy(charge=int(value)) for value in row]


def solve_1(values: InputType):
    print("Solve 1:", find_flashes(copy.deepcopy(values)))


def find_flashes(octopussies: InputType) -> int:
    return sum(step(octopussies) for _ in range(100))


def step(octopussies: InputType) -> int:
    init_step(octopussies)
    charge(octopussies)
    return count_flashed(octopussies)


@dataclass
class Octocell:
    octupus: Octopussy
    row: int
    col: int


def charge(octopussies: InputType):
    queue: SimpleQueue[Octocell] = SimpleQueue()
    height, width = octopussies.shape

    for row in range(height):
        for col in range(width):
            queue.put(Octocell(octopussies[row, col], row, col))
    while not queue.empty():
        cell = queue.get()
        flashed = cell.octupus.charge_and_flash()
        if flashed:
            [
                queue.put(Octocell(neighbor, n_row, n_col))
                for n_row, n_col in neighbor_indexes(cell.row, cell.col, height, width)
                if not (neighbor := octopussies[n_row, n_col]).flashed
            ]


def init_step(octopussies: InputType):
    init = numpy.vectorize(Octopussy.init_next_step)
    init(octopussies)


def count_flashed(octopussies: InputType) -> int:
    flashed = numpy.vectorize(Octopussy.has_flashed)
    return numpy.sum(flashed(octopussies))


def neighbor_indexes(
    row: int, col: int, height: int, width: int
) -> Set[Tuple[int, int]]:
    neighbors = set()
    if row > 0:
        neighbors.add((row - 1, col))
        if col > 0:
            neighbors.add((row - 1, col - 1))
        if col < width - 1:
            neighbors.add((row - 1, col + 1))
    if row < height - 1:
        neighbors.add((row + 1, col))
        if col > 0:
            neighbors.add((row + 1, col - 1))
        if col < width - 1:
            neighbors.add((row + 1, col + 1))
    if col > 0:
        neighbors.add((row, col - 1))
    if col < width - 1:
        neighbors.add((row, col + 1))
    return neighbors


def solve_2(values: InputType):
    print("Solve 2:", find_sync(values))


def find_sync(octopussies: InputType) -> int:
    count = 1
    height, width = octopussies.shape
    while step(octopussies) != height * width:
        count += 1
    return count


if __name__ == "__main__":
    input_values = read_input()
    print(input_values, sep="\n")
    step(input_values)
    # I have a 1 iteration offset for some reason :thinking: ...
    solve_1(input_values)
    solve_2(input_values)
