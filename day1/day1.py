from pathlib import Path
from typing import List, Tuple, Optional

year = 2020


def read_input() -> List[int]:
    with open(Path(Path(__file__).parent, "input")) as f:
        return sorted(list(map(int, f.read().split("\n"))))


def solve_1(values: List[int]):
    left, right = find_couple(values)
    print("Couple", left, right)
    print(left * right)


def find_couple(values: List[int], total=year) -> Optional[Tuple[int, int]]:
    for left in values:
        right = total - left
        if right < left:
            break
        if right in values:
            return left, right


def solve_2(values: List[int]):
    left, middle, right = find_triplet(values)
    print("Triplet", left, middle, right)
    print(left * middle * right)


def find_triplet(values: List[int], total=year) -> Tuple[int, int, int]:
    for index, left in enumerate(values):
        subyear = total - left
        try:
            middle, right = find_couple(values[index:], subyear)
            return left, middle, right
        except TypeError:
            continue


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
