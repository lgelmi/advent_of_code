from pathlib import Path
from typing import List


def read_input() -> List[int]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(int, f.read().split("\n")))


def solve_1(values: List[int]):
    print("Count", find_count(values))


def find_count(values: List[int]) -> int:
    return sum(before < after for before, after in zip(values, values[1:]))


def solve_2(values: List[int]):
    print("Count", find_triple_count(values))


def find_triple_count(values: List[int]) -> int:
    return find_count(triplets(values))


def triplets(values: List[int]) -> List[int]:
    return [sum(triplet) for triplet in zip(values, values[1:], values[2:])]


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
