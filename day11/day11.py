import itertools
import operator
from collections import Counter
import re
from functools import reduce
from pathlib import Path
from typing import List, Set, Dict, Tuple, Optional, NewType, Iterator

SeatsMapType = List[List[Optional[bool]]]
SEAT_CHARS = {"#": True, "L": False, ".": None}
SEAT_STATES = {v: k for k, v in SEAT_CHARS.items()}


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> SeatsMapType:
    return seats_from_string(content)


def fill_seats(seats: SeatsMapType) -> SeatsMapType:
    return [[True if state is not None else None for state in row] for row in seats]


def occupy_seats(seats: SeatsMapType) -> SeatsMapType:
    row_length = len(seats)
    row_seats = list(range(row_length))
    col_length = len(seats[0])
    col_seats = list(range(col_length))
    return [
        [
            should_be_occupied(row, col, seats, row_length, col_length)
            for col in col_seats
        ]
        for row in row_seats
    ]


def should_be_occupied(row: int, col: int, seats: SeatsMapType, row_length, col_length):
    seat = seats[row][col]
    if seat in [None, True]:
        return seat
    return all(
        seats[row][col] is not True
        for row, col in adjacent_indices(row, col, row_length, col_length)
    )


def leave_seats(seats: SeatsMapType) -> SeatsMapType:
    row_length = len(seats)
    row_seats = list(range(row_length))
    col_length = len(seats[0])
    col_seats = list(range(col_length))
    return [
        [
            update_left_state(row, col, seats, row_length, col_length)
            for col in col_seats
        ]
        for row in row_seats
    ]


def update_left_state(row: int, col: int, seats: SeatsMapType, row_length, col_length):
    seat = seats[row][col]
    if seat in [None, False]:
        return seat
    return [
        seats[row][col]
        for row, col in adjacent_indices(row, col, row_length, col_length)
    ].count(True) < 4


def adjacent_indices(row, col, row_length, col_length) -> List[Tuple[int, int]]:
    all_adjacent = list(
        itertools.starmap(
            lambda a, b: (row + a, col + b), itertools.product((0, -1, +1), (0, -1, +1))
        )
    )[1:]
    return [
        (row, col)
        for row, col in all_adjacent
        if 0 <= row < row_length and 0 <= col < col_length
    ]


def occupy_visible_seats(seats: SeatsMapType) -> SeatsMapType:
    row_length = len(seats)
    row_seats = list(range(row_length))
    col_length = len(seats[0])
    col_seats = list(range(col_length))
    return [
        [
            should_be_occupied_visible(row, col, seats, row_length, col_length)
            for col in col_seats
        ]
        for row in row_seats
    ]


def should_be_occupied_visible(
    row: int, col: int, seats: SeatsMapType, row_length, col_length
):
    seat = seats[row][col]
    if seat in [None, True]:
        return seat
    return visible_occupied(row, col, seats, row_length, col_length) == 0

def leave_visible_seats(seats: SeatsMapType) -> SeatsMapType:
    row_length = len(seats)
    row_seats = list(range(row_length))
    col_length = len(seats[0])
    col_seats = list(range(col_length))
    return [
        [
            update_left_visible_state(row, col, seats, row_length, col_length)
            for col in col_seats
        ]
        for row in row_seats
    ]


def update_left_visible_state(row: int, col: int, seats: SeatsMapType, row_length, col_length):
    seat = seats[row][col]
    if seat in [None, False]:
        return seat
    return visible_occupied(row, col, seats, row_length, col_length) < 5


def visible_occupied(row, col, seats: SeatsMapType, row_length, col_length) -> int:
    return sum(
        next((seats[x][y] for x, y in direction if seats[x][y] is not None), False)
        for direction in vision_generators(row, col, row_length, col_length)
    )


def vision_generators(
    row, col, row_length, col_length
) -> List[Iterator[Tuple[int, int]]]:
    directions = list(itertools.product((0, -1, +1), (0, -1, +1)))[1:]
    return [
        direction_generator(row, col, x, y, row_length, col_length)
        for x, y in directions
    ]


def direction_generator(row, col, x, y, row_length, col_length):
    row += x
    col += y
    while 0 <= row < row_length and 0 <= col < col_length:
        yield row, col
        row += x
        col += y


def seats_from_string(seats: str) -> SeatsMapType:
    rows = seats.split()
    return [[SEAT_CHARS[char] for char in row] for row in rows]


def seats_to_str(seats: SeatsMapType) -> str:
    return "\n".join(["".join(SEAT_STATES[state] for state in row) for row in seats])


def find_stable_seats(seats: SeatsMapType) -> SeatsMapType:
    initial_state = fill_seats(seats)
    step_behaviours = [leave_seats, occupy_seats]
    for behaviour in itertools.cycle(step_behaviours):
        new_state = behaviour(initial_state)
        if new_state == initial_state:
            return new_state
        initial_state = new_state

def find_stable_visible_seats(seats: SeatsMapType) -> SeatsMapType:
    initial_state = fill_seats(seats)
    step_behaviours = [leave_visible_seats, occupy_visible_seats]
    for behaviour in itertools.cycle(step_behaviours):
        new_state = behaviour(initial_state)
        if new_state == initial_state:
            return new_state
        initial_state = new_state


def solve_1(values):
    print("--------------- 1 ---------------")
    print(seats_to_str(find_stable_seats(values)).count("#"))


def solve_2(values):
    print("--------------- 2 ---------------")
    print(seats_to_str(find_stable_visible_seats(values)).count("#"))

# This solution sucks, but I'm tired today
if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
