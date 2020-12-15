from pathlib import Path
from typing import List, Dict


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> List[int]:
    return list(map(int, content.split(",")))


def initialize_memory(start: List[int]) -> Dict[int, int]:
    return {value: index for index, value in enumerate(start, 1)}


def get_next_number(current: int, turn: int, memory: Dict[int, int]) -> int:
    return (turn - memory[current]) if current in memory else 0


def play_memory(start: List[int], limit: int) -> int:
    memory = initialize_memory(start[:-1])
    current = start[-1]
    for turn in range(len(start), limit):
        next = get_next_number(current, turn, memory)
        # print(turn, current, memory, next)
        memory[current] = turn
        current = next
    return current


def solve_1(values):
    print("--------------- 1 ---------------")
    print(play_memory(values, 2020))


def solve_2(values):
    print("--------------- 2 ---------------")
    print(play_memory(values, 30000000))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
