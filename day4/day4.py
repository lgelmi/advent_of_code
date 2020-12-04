from pathlib import Path
from typing import Dict, List


class PassportScanner:
    REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

    def __init__(self, required_fields=None):
        self.required_fields = required_fields or self.REQUIRED_FIELDS

    def validate_fields(self, fields: Dict):
        return all(field in fields for field in self.required_fields)


class StrictPassportScanner:
    def __init__(self):
        self.validators = {
            "byr": self.validate_byr,
            "iyr": self.validate_iyr,
            "eyr": self.validate_eyr,
            "hgt": self.validate_hgt,
            "hcl": self.validate_hcl,
            "ecl": self.validate_ecl,
            "pid": self.validate_pid,
            "cid": self.validate_cid,
        }

    def validate_fields(self, fields: Dict[str, str]):
        return all(
            field in fields and self.validators[field](fields[field])
            for field in self.validators
        )

    @classmethod
    def validate_byr(cls, value: str) -> bool:
        return cls.validate_number(value, 1920, 2002, 4)

    @classmethod
    def validate_iyr(cls, value: str) -> bool:
        return cls.validate_number(value, 2010, 2020, 4)

    @classmethod
    def validate_eyr(cls, value: str) -> bool:
        return cls.validate_number(value, 2020, 2030, 4)

    @classmethod
    def validate_hgt(cls, value: str) -> bool:
        if value.endswith("cm"):
            return cls.validate_number(value[:-2], 150, 193)
        if value.endswith("in"):
            return cls.validate_number(value[:-2], 59, 76)
        return False

    @classmethod
    def validate_number(cls, str_value, left, right, digits=None) -> bool:
        if not str_value.isdigit():
            return False

        if digits and len(str_value) != digits:
            return False

        return left <= int(str_value) <= right

    @classmethod
    def validate_hcl(cls, value: str) -> bool:
        return (
            len(value) == 7
            and value.startswith("#")
            and all("0" <= char <= "9" or "a" <= char <= "f" for char in value[1:])
        )

    @classmethod
    def validate_ecl(cls, value: str) -> bool:
        return value in {
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        }

    @classmethod
    def validate_pid(cls, value: str) -> bool:
        return len(value) == 9 and value.isdigit()

    @classmethod
    def validate_cid(cls, _: str) -> bool:
        return False


class HackedStrictPassportScanner(StrictPassportScanner):
    def __init__(self):
        super().__init__()
        del self.validators["cid"]


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
    passport_dicts = list(map(parse_passport, values))
    hacked_scanner = HackedStrictPassportScanner()
    print(sum(map(hacked_scanner.validate_fields, passport_dicts)))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
