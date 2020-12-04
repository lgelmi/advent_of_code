import functools
import itertools
import operator
from pathlib import Path
from typing import Dict, Iterable, List


class PassportScanner:
    REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

    def __init__(self, required_fields=None):
        self.required_fields = required_fields or self.REQUIRED_FIELDS

    def validate_fields(self, fields: Dict):
        return all(field in fields for field in self.required_fields)


def read_input() -> List[str]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(f.read().split("\n\n"))


def parse_passport(passport: str) -> Dict:
    pairs = passport.split()
    return {left: right for left, right in map(lambda x: x.split(":"), pairs)}


def solve_1(values: List[str]):
    passport_dicts = list(map(parse_passport, values))
    hacked_scanner = PassportScanner(PassportScanner.REQUIRED_FIELDS - {"cid"})
    print(sum(map(hacked_scanner.validate_fields, passport_dicts)))


def solve_2(values: List[str]):
    pass


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
