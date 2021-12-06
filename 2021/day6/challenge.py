from collections import Counter
from functools import reduce
from pathlib import Path
from typing import List

InputType = List[int]


class Fornicator9000(Counter):

    PERIOD = 6
    YOUTH = 2

    def fornicate(self) -> "Fornicator9000":
        new_fishes = self[0]
        fornicator = Fornicator9000(
            {value - 1: number for value, number in self.items()}
        )
        fornicator[self.PERIOD] += fornicator[-1]
        del fornicator[-1]
        fornicator[self.PERIOD + self.YOUTH] = new_fishes
        return fornicator


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(int, f.read().split(",")))


def solve_1(values: InputType):
    print(simulate_growth(values, 80))


def simulate_growth(values: InputType, days: int) -> int:
    fornicator = Fornicator9000(values)
    for _ in range(days):
        fornicator = fornicator.fornicate()
    return sum(fornicator.values())


def solve_2(values: InputType):
    print(simulate_growth(values, 256))


if __name__ == "__main__":
    values = read_input()
    print(*values, sep="\n")
    solve_1(values)
    solve_2(values)
