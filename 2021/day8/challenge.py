from pathlib import Path
from typing import Dict, List, Literal, Set, Tuple

InputType = List[Tuple[List[str], List[str]]]

Digit = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
CodeType = Dict[Digit, Set[str]]


class SevenDigitDecoder:
    def __init__(self, code: CodeType):
        self.code = code

    @classmethod
    def from_random_entry(cls, entry: List[str]) -> "SevenDigitDecoder":
        return cls(code=cls.code_from_random_entry(entry))

    @classmethod
    def code_from_random_entry(cls, entry: List[str]) -> CodeType:
        code = {}
        entry = [set(digit) for digit in entry]
        while entry:
            for digit in entry.copy():
                try:
                    value = cls.code_match(digit, code)
                    code[value] = digit
                    entry.remove(digit)
                except KeyError:
                    pass
        return code

    @classmethod
    def code_match(cls, digit: Set[str], code: CodeType) -> Digit:
        match len(digit):
            case 2:
                return 1
            case 3:
                return 7
            case 4:
                return 4
            case 5:
                if code[1].issubset(digit):
                    return 3
                if digit.issubset(code[6]):
                    return 5
                return 2
            case 6:
                if not code[1].issubset(digit):
                    return 6
                if code[3].issubset(digit):
                    return 9
                else:
                    return 0
            case 7:
                return 8
        raise ValueError(f"Can't match {digit}")

    def decode(self, values: List[str]) -> int:
        return int("".join(str(self.decode_value(value)) for value in values))

    def decode_value(self, value: str) -> Digit:
        value = set(value)
        return next(digit for digit, segment in self.code.items() if value == segment)


def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        rows = f.read().split("\n")
        return [parse_row(row) for row in rows]


def parse_row(row: str) -> Tuple[List[str], List[str]]:
    left, right = row.split(" | ")
    return left.split(), right.split()


def solve_1(values: InputType):
    print("Solve 1:", count_naive(values))


def count_naive(entries: InputType) -> int:
    return sum(
        len(digit) in (2, 3, 4, 7)
        for connections, digits in entries
        for digit in digits
    )


def solve_2(values: InputType):
    print("Solve 2:", sum_outputs(values))

def sum_outputs(entries: InputType) -> int:
    return sum(SevenDigitDecoder.from_random_entry(entry).decode(encoded) for (entry, encoded) in entries)

if __name__ == "__main__":
    values = read_input()
    print(*values, sep="\n")
    solve_1(values)
    solve_2(values)
