import itertools
from pathlib import Path
from typing import List, Tuple


def read_input():
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_values(f.read())


def parse_values(content: str) -> Tuple[int, List[int]]:
    earliest, buses = content.split()
    return int(earliest), [int(bus) if bus != "x" else None for bus in buses.split(",")]


def find_starts(start: int, buses: List[int]):
    return [
        (((start // bus) + (0 if start % bus == 0 else 1)) * bus)
        if bus is not None
        else bus
        for bus in buses
    ]


def find_earliest(start: int, buses: List[int]):
    starts = find_starts(start, buses)
    earliest_time = min(s for s in starts if s is not None)
    return buses[starts.index(earliest_time)], (earliest_time - start)


def solve_1(values):
    print("--------------- 1 ---------------")
    bus, time = find_earliest(*values)
    print(bus * time)


def find_couple_increment(start, step, incr, modulo):
    return next(
        timestamp
        for timestamp in itertools.count(start, step)
        if not (timestamp + incr) % modulo
    )

def find_timestamp(buses: List[int]):
    start = step = buses[0]
    for increment, modulo in ((i+1, b) for i,b in enumerate(buses[1:]) if b is not None):
        start = find_couple_increment(start, step, increment, modulo)
        step *= modulo
    return start

def solve_2(values):
    _, buses = values
    print("--------------- 2 ---------------")
    print(find_timestamp(buses))


if __name__ == "__main__":
    values = read_input()
    solve_1(values)
    solve_2(values)
