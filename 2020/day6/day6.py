from pathlib import Path
from typing import List, Set


def read_input() -> List[str]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return f.read().split("\n\n")


def group_answers(answers: str) -> Set:
    return set().union(*answers) - set("\n")


def solve_1(groups: List[str]):
    print(sum(len(group_answers(group)) for group in groups))


def group_common_answers(answers: str) -> Set:
    answers = answers.split()
    base = set(answers[0])
    try:
        return base.intersection(*answers[1:]) - set("\n")
    except IndexError:
        return base


def solve_2(groups: List[str]):
    print(sum(len(group_common_answers(group)) for group in groups))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
