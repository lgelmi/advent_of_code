import functools
import itertools
from pathlib import Path
from typing import Iterable, List


def read_input() -> List[str]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(str.strip, f.read().split("\n")))


def traversed_tree(geology, right, down) -> int:
    return traverse(geology, right, down).count("#")


def traverse(geology, right, down) -> str:
    return "".join(
        level[position]
        for level, position in zip(
            geology[down::down], module_count(right, right, module=len(geology[0]))
        )
    )


def module_count(start, step: int = 1, module=1) -> Iterable[int]:
    count = itertools.count(start, step)
    while True:
        yield next(count) % module


def solve_1(values: List[str]):
    print(traversed_tree(values, 3, 1))


def solve_2(values: List[str]):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    traversed = [traversed_tree(values, right, down) for right, down in slopes]
    print(functools.reduce(lambda x, y: x * y, traversed))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
