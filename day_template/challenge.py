from pathlib import Path
from typing import List

InputType = List[str]


# noinspection DuplicatedCode
def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return f.read().split("\n")


def solve_1(values: InputType):
    print("Solve 1:", ...)


def solve_2(values: InputType):
    print("Solve 2:", ...)


if __name__ == "__main__":
    input_values = read_input()
    print(input_values, sep="\n")
    solve_1(input_values)
    solve_2(input_values)
