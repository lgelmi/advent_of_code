from collections import deque
from functools import reduce
from pathlib import Path
from typing import Dict, Iterator, List, Literal, Optional, Set, Tuple

InputType = List[str]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return f.read().split("\n")


def solve_1(values: InputType):
    print("Solve 1:", sum_corrupted(values))


chunks = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

corruption_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def sum_corrupted(lines: InputType) -> int:
    return sum(corruption_scores[corrupted] for corrupted in get_corrupted(lines))


def get_corrupted(lines: InputType) -> List[str]:
    return [
        corrupted for line in lines if (corrupted := first_corrupted(line)) is not None
    ]


def first_corrupted(line: str) -> Optional[str]:
    stack = deque()
    for char in line:
        if char in chunks:
            stack.append(chunks[char])
        elif char != stack.pop():
            return char


def solve_2(values: InputType):
    print("Solve 2:", middle_incomplete_scores(values))


incomplete_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def middle_incomplete_scores(lines: InputType) -> int:
    scores = [get_incomplete_score(line) for line in lines if not first_corrupted(line)]
    return sorted(scores)[len(scores) // 2]


def get_incomplete_score(line: str) -> int:
    return reduce(
        lambda base, char: base * 5 + incomplete_scores[char],
        generate_completion_chars(line),
        0,
    )


def generate_completion_chars(line: str) -> Iterator[str]:
    stack = deque()
    for char in line:
        if char in chunks:
            stack.append(chunks[char])
        elif not stack:
            break
        elif char != (expected := stack.pop()):
            raise ValueError(f"Expected {expected}, but found {char} instead.")
    while stack:
        yield stack.pop()


if __name__ == "__main__":
    values = read_input()
    print(values, sep="\n")
    solve_1(values)
    solve_2(values)
