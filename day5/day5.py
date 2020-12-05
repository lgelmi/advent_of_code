from pathlib import Path
from typing import List, Set


def read_input() -> List[str]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(f.read().split("\n"))


def decode_row(seat: str) -> int:
    row_code = seat[:7]
    row_code = row_code.replace("F", "0")
    row_code = row_code.replace("B", "1")
    return int(row_code, 2)


def decode_column(seat: str) -> int:
    col_code = seat[-3:]
    col_code = col_code.replace("L", "0")
    col_code = col_code.replace("R", "1")
    return int(col_code, 2)


def decode_seat_id(seat: str) -> int:
    return seat_id(decode_row(seat), decode_column(seat))


def seat_id(row, column):
    return row * 8 + column


def highest_pass(seats: List[str]) -> str:
    # noinspection PyTypeChecker
    return max(map(decode_seat_id, seats))


def solve_1(values: List[str]):
    print(highest_pass(values))


ALL_ID = [seat_id(row, column) for row in range(128) for column in range(8)]


def get_seat(ids: Set[int]) -> int:
    for left, id, right in zip(ALL_ID[:-2], ALL_ID[1:-1], ALL_ID[2:]):
        if id not in ids and left in ids and right in ids:
            return id


def solve_2(values: List[str]):
    # noinspection PyTypeChecker
    print(get_seat(ids=set(map(decode_seat_id, values))))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
