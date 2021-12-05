from dataclasses import dataclass
from itertools import chain
from pathlib import Path
from typing import List

import numpy


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, raw: str) -> "Point":
        return cls(*map(int, raw.split(",")))


@dataclass
class Segment:
    start: Point
    end: Point

    @classmethod
    def from_str(cls, raw: str) -> "Segment":
        return cls(*map(Point.from_str, raw.split(" -> ")))

    def draw_on_board(self, board: numpy.ndarray, diagonal=False):
        self.draw_horizontally_on_board(board)
        self.draw_vertically_on_board(board)
        if diagonal:
            self.draw_diagonally_on_board(board)

    def draw_horizontally_on_board(self, board: numpy.ndarray):
        if (y := self.start.y) == self.end.y:
            start, end = (
                (start, end)
                if (start := self.start.x) < (end := self.end.x)
                else (end, start)
            )
            board[y, start : end + 1] += 1

    def draw_vertically_on_board(self, board: numpy.ndarray):
        if (x := self.start.x) == self.end.x:
            start, end = (
                (start, end)
                if (start := self.start.y) < (end := self.end.y)
                else (end, start)
            )
            board[start : end + 1, x] += 1

    def draw_diagonally_on_board(self, board: numpy.ndarray):
        if self.start.x != self.end.x and self.start.y != self.end.y:
            x_step = 1 if self.start.x < self.end.x else -1
            y_step = 1 if self.start.y < self.end.y else -1

            board[
                range(self.start.y, self.end.y + y_step, y_step),
                range(self.start.x, self.end.x + x_step, x_step),
            ] += 1


InputType = List[Segment]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(Segment.from_str, f.read().split("\n")))


def solve_1(values: InputType):
    print(get_dangerous_point_count(values))


def get_dangerous_point_count(segments: InputType) -> int:
    board = draw_board(segments)
    draw_segments_on_board(segments, board)
    # noinspection PyTypeChecker
    return numpy.sum(board >= 2)


def draw_board(segments: InputType) -> numpy.ndarray:
    return numpy.zeros(
        (
            max(
                chain(
                    (segment.end.x + 1 for segment in segments),
                    (segment.start.x + 1 for segment in segments),
                )
            ),
            max(
                chain(
                    (segment.start.y + 1 for segment in segments),
                    (segment.end.y + 1 for segment in segments),
                )
            ),
        )
    )


def draw_segments_on_board(segments: InputType, board: numpy.ndarray, diagonal=False):
    for segment in segments:
        segment.draw_on_board(board, diagonal)


def solve_2(values: InputType):
    print(get_dangerous_point_count_diagonal(values))


def get_dangerous_point_count_diagonal(segments: InputType) -> int:
    board = draw_board(segments)
    draw_segments_on_board(segments, board, True)
    # noinspection PyTypeChecker
    return numpy.sum(board >= 2)


if __name__ == "__main__":
    values = read_input()
    print(*values, sep="\n")
    solve_1(values)
    solve_2(values)
