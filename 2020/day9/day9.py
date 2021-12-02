from collections import Counter
import re
from pathlib import Path
from typing import List, Set, Dict, Tuple


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> List[int]:
    return [int(value) for value in content.split()]


class XMASMissingFounder:
    # Only work as long as no duplicate exists...

    def __init__(self, preamble: List[int]):
        self.mapped_sums: Dict[int, Set[int]] = {}
        for value in preamble:
            self.add(value)

    def add(self, value):
        if value in self.mapped_sums:
            raise ValueError(
                f"Can't add {value}: XMAS does not support duplicate values."
            )
        for left, sums in self.mapped_sums.items():
            self.mapped_sums[left].add(left + value)
        self.mapped_sums[value] = {value + left for left in self.mapped_sums}

    def remove(self, value):
        del self.mapped_sums[value]
        for left, sums in self.mapped_sums.items():
            self.mapped_sums[left].remove(left + value)

    def __contains__(self, value):
        return any(value in sums for sums in self.mapped_sums.values())


def first_missing(values, preamble_length) -> int:
    xmas = XMASMissingFounder(values[:preamble_length])
    for i, value in enumerate(values[preamble_length:], start=preamble_length):
        if value not in xmas:
            return value
        xmas.remove(values[i - preamble_length])
        xmas.add(value)


def get_consecutive(values, target) -> List[int]:
    candidates = []
    for value in values:
        candidates.append(value)
        while sum(candidates) > target:
            candidates.pop(0)
        if sum(candidates) == target and len(candidates) >= 2:
            return candidates


def solve_1(values):
    print("--------------- 1 ---------------")
    print(first_missing(values, 25))


def solve_2(values):
    print("--------------- 2 ---------------")
    missing = first_missing(values, 25)
    # I'm in a hurry, sorry
    consecutives = get_consecutive(values, missing)
    print(min(consecutives) + max(consecutives))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
