from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import numpy


@dataclass
class FoldInstruction:
    vertical: bool
    position: int

    @classmethod
    def from_str(cls, value: str) -> "FoldInstruction":
        left, right = value.split("=")
        return cls(vertical=left[-1] == "y", position=int(right))


@dataclass
class TransparentPaper:

    paper: numpy.array

    @classmethod
    def from_str(cls, value: str) -> "TransparentPaper":
        indexes = numpy.array(
            [list(map(int, row.split(","))) for row in value.split("\n")]
        )
        x_max, y_max = indexes.max(axis=0)
        paper = numpy.zeros((x_max + 1, y_max + 1), dtype=bool).transpose()
        for y, x in indexes:
            paper[x][y] = True
        return cls(paper)

    def fold(self, instruction: FoldInstruction) -> "TransparentPaper":
        # noinspection PyArgumentList
        return (
            self.fold_vertically if instruction.vertical else self.fold_horizontally
        )(position=instruction.position)

    def fold_horizontally(self, position: int) -> "TransparentPaper":
        paper = self.paper
        return TransparentPaper(paper[:, :position] | paper[:, :position:-1])

    def fold_vertically(self, position: int) -> "TransparentPaper":
        paper = self.paper
        return TransparentPaper(paper[:position] | paper[:position:-1])

    def count_empty(self):
        return numpy.sum(self.paper)


InputType = Tuple[TransparentPaper, List[FoldInstruction]]


# noinspection DuplicatedCode
def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_input(f.read())


def parse_input(content: str) -> InputType:
    upper, lower = content.split("\n\n")
    return (
        TransparentPaper.from_str(upper),
        [FoldInstruction.from_str(row) for row in lower.split("\n")],
    )


def parse_row(row: str) -> str:
    return row


def solve_1(values: InputType):
    print("Solve 1:", count_first_fold(*values))


def count_first_fold(paper: TransparentPaper, instructions: List[FoldInstruction]):
    return paper.fold(instructions[0]).count_empty()


def solve_2(values: InputType):
    print("Solve 2:", *[encode_row(row) for row in fold(*values).paper], sep="\n")


def encode_row(row):
    return " ".join("#" if x else "." for x in row)


def fold(paper: TransparentPaper, instructions: List[FoldInstruction]):
    for instruction in instructions:
        paper = paper.fold(instruction)
    return paper


if __name__ == "__main__":
    input_values = read_input()
    print(input_values, sep="\n")
    solve_1(input_values)
    solve_2(input_values)
