import dataclasses
import functools

from pathlib import Path
from typing import List, Iterator


def read_input() -> List[str]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(str.strip, f.read().split("\n")))


def traverse(geology, right, down) -> str:
    return "".join(level[position] for level, position in zip(geology[::down], range(0, len(geology[0]), right)))


def solve_1(values: List[str]):
    traversed = traverse(values, 3, 1)
    print(traversed)
    print(traversed.count("#"))


def solve_2(values: List[str]):
    pass


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
