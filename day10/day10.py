import operator
from collections import Counter
import re
from functools import reduce
from pathlib import Path
from typing import List, Set, Dict, Tuple


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> List[int]:
    return sorted([int(value) for value in content.split()])


def jolt_steps(values: List[int]) -> List[int]:
    diff = [right - left for left, right in zip(values, values[1:])]
    diff.insert(0, values[0])
    diff.append(3)
    return diff


def count_steps(steps: List[int]) -> Counter:
    return Counter(steps)


def jolt_difference(values: List[int]) -> int:
    counter = count_steps(jolt_steps(values))
    return counter[1] * counter[3]


combination_count = {1: 1, 2: 2, 3: 4}


def get_combination_count(consecutive_ones):
    if consecutive_ones <= 0:
        return 1
    if consecutive_ones in combination_count:
        return combination_count[consecutive_ones]

    new_starts = get_combination_count(consecutive_ones - 1) * 2 - 1
    combination_count[consecutive_ones] = new_starts
    return new_starts


def count_consecutive_element(values, element) -> Counter:
    counter = Counter()
    count = 0
    for value in values:
        if value == element:
            count += 1
        else:
            counter[count] += 1
            count = 0
    return counter


def count_combination(values: List[int]) -> int:
    consecutive_ones = count_consecutive_element(jolt_steps(values), 1)
    return reduce(
        operator.mul,
        (
            get_combination_count(length) ** count
            for length, count in consecutive_ones.items()
        )
    )


def solve_1(values):
    print("--------------- 1 ---------------")
    print(jolt_difference(values))


def solve_2(values):
    print("--------------- 2 ---------------")
    print(count_combination(values))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
