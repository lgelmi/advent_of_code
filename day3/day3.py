import itertools

from pathlib import Path
from typing import List, Iterator, Iterable, Sized


def read_input() -> List[str]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(str.strip, f.read().split("\n")))


def traverse(geology, right, down) -> str:
    return "".join(
        level[position]
        for level, position in zip(geology[down::down], module_count(right, right, module=len(geology[0])))
    )


def module_count(start, step: int = 1, module=1) -> Iterable[int]:
    count = itertools.count(start, step)
    while True:
        yield next(count) % module


def solve_1(values: List[str]):
    traversed = traverse(values, right=3, down=1)
    print(traversed)
    print(traversed.count("#"))


def solve_2(values: List[str]):
    pass


if __name__ == "__main__":
    values = read_input()

    print([v for _,v in zip(range(5), module_count(1, 3))])
    solve_1(values)
    solve_2(values)
