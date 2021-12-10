from pathlib import Path
from typing import Dict, List, Literal, Set, Tuple

import numpy

InputType = numpy.array

Digit = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
CodeType = Dict[Digit, Set[str]]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return get_array(f.read().split("\n"))


def get_array(file_content: List[str]) -> InputType:
    return numpy.array([list(map(int, row)) for row in file_content])


def solve_1(values: InputType):
    print("Solve 1:", sum_minimums(values))


def sum_minimums(heights: InputType) -> int:
    minimums = get_minimums(heights)
    return sum(minimums) + len(minimums)


def get_minimums(heights: numpy.array) -> List[int]:
    height, width = heights.shape
    return [
        heights[row, col]
        for row in range(height)
        for col in range(width)
        if is_minimum(heights, row, col, height, width)
    ]


def is_minimum(
    heights: numpy.array, row: int, col: int, height: int, width: int
) -> bool:
    return all(
        heights[neighbor] > heights[row, col]
        for neighbor in index_neighbors(row, col, height, width)
    )


def index_neighbors(
    row: int, col: int, height: int, width: int
) -> Set[Tuple[int, int]]:
    neighbors = set()
    if row > 0:
        neighbors.add((row - 1, col))
    if row < height - 1:
        neighbors.add((row + 1, col))
    if col > 0:
        neighbors.add((row, col - 1))
    if col < width - 1:
        neighbors.add((row, col + 1))
    return neighbors


def solve_2(values: InputType):
    print("Solve 2:", get_top_basins(values))


def get_top_basins(heights: numpy.array) -> int:
    height, width = heights.shape
    return numpy.prod(
        sorted(
            (
                get_basin_size(heights, row, col, height, width)
                for row, col in get_minimum_indexes(heights)
            ),
            reverse=True,
        )[:3]
    )


def get_minimum_indexes(heights: numpy.array) -> List[Tuple[int, int]]:
    height, width = heights.shape
    return [
        (row, col)
        for row in range(height)
        for col in range(width)
        if is_minimum(heights, row, col, height, width)
    ]


def get_basin_size(
    heights: numpy.array, row: int, col: int, height: int, width: int
) -> int:
    points = {
        (row, col),
    }
    path = {
        (row, col),
    }
    while path:
        row, col = path.pop()
        value = heights[row, col]
        if value == 8:
            continue
        step = {
            neighbor
            for neighbor in index_neighbors(row, col, height, width)
            if (neighbor_height := heights[neighbor]) > value and neighbor_height != 9
        }
        path |= step - points
        points |= step
    return len(points)


if __name__ == "__main__":
    values = read_input()
    print(values, sep="\n")
    solve_1(values)
    solve_2(values)
