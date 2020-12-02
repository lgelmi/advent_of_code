import dataclasses
from pathlib import Path
from typing import List, Tuple, Optional


@dataclasses.dataclass
class TobogganPasswordPolicy:
    minimum: int
    maximum: int
    character: str

    @classmethod
    def from_str(cls, code: str) -> "TobogganPasswordPolicy":
        minimum, right = code.split("-")
        maximum, character = right.split()
        return cls(int(minimum), int(maximum), character)

    def validate(self, password: str) -> bool:
        return self.minimum <= password.count(self.character) <= self.maximum


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


def read_input() -> List[TobogganPasswordEntry]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return list(map(TobogganPasswordEntry.from_str, f.read().split("\n")))


def solve_1(values: List[TobogganPasswordEntry]):
    print(sum(list(map(TobogganPasswordEntry.validate, values))))


#
# def find_couple(values: List[int], total=year) -> Optional[Tuple[int, int]]:
#     for left in values:
#         right = total - left
#         if right < left:
#             break
#         if right in values:
#             return left, right
#
#
# def solve_2(values: List[int]):
#     left, middle, right = find_triplet(values)
#     print("Triplet", left, middle, right)
#     print(left * middle * right)
#
#
# def find_triplet(values: List[int], total=year) -> Tuple[int, int, int]:
#     for index, left in enumerate(values):
#         subyear = total - left
#         try:
#             middle, right = find_couple(values[index:], subyear)
#             return left, middle, right
#         except TypeError:
#             continue
#

if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    # solve_2(values)
