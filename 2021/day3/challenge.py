import numpy

from pathlib import Path
from typing import List, Callable, Any

from collections import Counter

InputType = List[List[int]]


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return [list(map(int, code)) for code in f.read().split("\n")]


def solve_1(values: InputType):
    matrix = numpy.array(values)
    print(get_power_consumption(matrix))


def get_power_consumption(matrix: numpy.ndarray) -> int:
    polarity = get_most_commons(matrix)
    gamma = bin_list_to_dec(polarity)
    epsilon = bin_list_to_dec([not value for value in polarity])
    return gamma * epsilon


def get_most_commons(matrix: numpy.ndarray) -> List[int]:
    return [get_most_common(column) for column in matrix.transpose()]


def get_most_common(array: numpy.array) -> Any:
    return (Counter({1: 0, 0: 0}) + Counter(array)).most_common(1)[0][0]


def bin_list_to_dec(binaries: List[int]):
    decimal = 0
    for bin in binaries:
        decimal = (decimal << 1) | bin
    return decimal


def solve_2(values: InputType):
    matrix = numpy.array(values)
    print(get_life_support_rating(matrix))


def get_life_support_rating(matrix: numpy.ndarray) -> int:
    oxigen = bin_list_to_dec(filter_bits(matrix, oxigen_filter))
    co2 = bin_list_to_dec(filter_bits(matrix, co2_filter))
    return oxigen * co2


def oxigen_filter(column: numpy.array) -> numpy.array:
    return column == get_most_common(column)


def co2_filter(column: numpy.array) -> numpy.array:
    return column == (0 if get_most_common(column) == 1 else 1)


def filter_bits(
    matrix: numpy.ndarray, bit_filter: Callable[[numpy.array], numpy.array]
) -> numpy.array:
    for index in range(matrix.shape[1]):
        matrix = filter_rows(matrix, bit_filter, index)
        if matrix.shape[0] == 1:
            return matrix[0]


def filter_rows(
    matrix: numpy.ndarray,
    bit_filter: Callable[[numpy.array], numpy.array],
    index: int,
) -> numpy.ndarray:
    return matrix[bit_filter(matrix[:, index])]


if __name__ == "__main__":
    values = read_input()
    print(values)
    solve_1(values)
    solve_2(values)
