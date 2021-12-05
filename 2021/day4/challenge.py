from itertools import chain

import numpy

from pathlib import Path
from typing import List, Tuple, Optional


class Board:
    def __init__(self, numbers: List[List[int]]):
        self.numbers = numpy.array(numbers)
        self.marks = numpy.zeros(self.numbers.shape, dtype=bool)

    @classmethod
    def from_str(cls, board_string: str) -> "Board":
        return Board([list(map(int, row.split())) for row in board_string.split("\n")])

    def __repr__(self) -> str:
        return str(
            numpy.char.add(
                numpy.char.add(self.marks_string(), " "), self.numbers.astype(str)
            )
        )

    def marks_string(self) -> numpy.array:
        return numpy.where(self.marks, "X", "O")

    def mark_and_win(self, number) -> bool:
        self.mark(number)
        return self.has_won()

    def mark(self, number: int):
        self.marks[self.numbers == number] = True

    def has_won(self) -> bool:
        return any(all(line) for line in chain(self.marks, self.marks.transpose()))

    def unmarked_sum(self) -> int:
        return (self.numbers * ~self.marks).sum()


InputType = Tuple[List[int], List[Board]]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        numbers, _, boards = f.read().split("\n", maxsplit=2)
        numbers = list(map(int, numbers.split(",")))
        return numbers, [
            Board.from_str(board_string) for board_string in boards.split("\n\n")
        ]


def solve_1(values: InputType):
    numbers, boards = values
    print(get_winner_score(numbers, boards))


def get_winner_score(numbers: List[int], boards: List[Board]) -> int:
    for extracted in numbers:
        if winner := get_winner(extracted, boards):
            return winner.unmarked_sum() * extracted


def get_winner(number: int, boards: List[Board]) -> Optional[Board]:
    return next((board for board in boards if board.mark_and_win(number)), None)


def solve_2(values: InputType):
    numbers, boards = values
    print(get_loser_score(numbers, boards))


def get_loser_score(numbers: List[int], boards: List[Board]) -> int:
    remaining = boards
    for extracted in numbers:
        losers = get_losers(extracted, remaining)
        if len(remaining) == 1 and remaining[0].has_won():
            return remaining[0].unmarked_sum() * extracted
        remaining = losers


def get_losers(number: int, boards: List[Board]) -> List[Board]:
    return [board for board in boards if not board.mark_and_win(number)]


if __name__ == "__main__":
    values = read_input()
    print(*values, sep="\n")
    solve_1(values)
    solve_2(values)
