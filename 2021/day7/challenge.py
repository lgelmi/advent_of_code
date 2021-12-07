from functools import partial
from pathlib import Path
from typing import List

InputType = List[int]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(int, f.read().split(",")))


def solve_1(values: InputType):
    print("Solve 1:", find_fuel(values))


def find_fuel(crabs: InputType) -> int:
    return fuel_consumption(find_position(crabs), crabs)


def find_position(crabs: InputType) -> int:
    return min(range(max(crabs)), key=partial(fuel_consumption, crabs=crabs))


def fuel_consumption(position: int, crabs: InputType) -> int:
    return sum(abs(crab - position) for crab in crabs)


def solve_2(values: InputType):
    print("Solve 2:", find_triangular_fuel(values))


def find_triangular_fuel(crabs: InputType) -> int:
    return triangular_fuel_consumption(find_triangular_position(crabs), crabs)


def find_triangular_position(crabs: InputType) -> int:
    return min(range(max(crabs)), key=partial(triangular_fuel_consumption, crabs=crabs))


def triangular_fuel_consumption(position: int, crabs: InputType) -> int:
    return sum(triangular_number(abs(crab - position)) for crab in crabs)


def triangular_number(value: int) -> float:
    return value * (value + 1) / 2


if __name__ == "__main__":
    values = read_input()
    print(*values, sep="\n")
    solve_1(values)
    solve_2(values)
