import dataclasses
import functools

from pathlib import Path
from typing import List


@dataclasses.dataclass
class TobogganPasswordPolicy:
    positions: List[int]
    character: str

    @classmethod
    def from_str(cls, code: str) -> "TobogganPasswordPolicy":
        left, character = code.split()
        positions = map(int, left.split("-"))
        return cls(sorted(list(positions)), character)

    def validate(self, password: str) -> bool:
        minimum, maximum = self.positions[0], self.positions[-1]
        return minimum <= password.count(self.character) <= maximum

    def official_validate(self, password: str) -> bool:
        at_positions = map(
            lambda position: password[position - 1] == self.character, self.positions
        )
        return functools.reduce(lambda x, y: x ^ y, at_positions)


@dataclasses.dataclass
class TobogganPasswordEntry:
    policy: TobogganPasswordPolicy
    password: str

    @classmethod
    def from_str(cls, code: str) -> "TobogganPasswordEntry":
        left, right = code.split(":")
        policy = TobogganPasswordPolicy.from_str(left)
        password = right.strip()
        return cls(policy, password)

    def validate(self) -> bool:
        return self.policy.validate(self.password)

    def official_validate(self) -> bool:
        return self.policy.official_validate(self.password)


def read_input() -> List[TobogganPasswordEntry]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(TobogganPasswordEntry.from_str, f.read().split("\n")))


def solve_1(values: List[TobogganPasswordEntry]):
    print(sum(list(map(TobogganPasswordEntry.validate, values))))


def solve_2(values: List[TobogganPasswordEntry]):
    print(sum(list(map(TobogganPasswordEntry.official_validate, values))))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
