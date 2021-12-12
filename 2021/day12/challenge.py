import dataclasses
from collections import namedtuple
from dataclasses import dataclass, field
from pathlib import Path
from queue import LifoQueue
from typing import Dict, Iterator, List, Set, Tuple


@dataclass
class Cave:
    name: str
    edges: Set["Cave"] = field(default_factory=set)

    def __hash__(self):
        return hash(self.name)

    def __repr__(self) -> str:
        return f"Cave({self.name} -> [{','.join(node.name for node in self.edges)}])"

    def add_edge(self, cave: "Cave"):
        self.edges.add(cave)

    def is_big(self) -> bool:
        return self.name.isupper()


class CaveMap(dict):
    def add_edge(self, left: str, right: str):
        left = self.add_node(left)
        right = self.add_node(right)
        left.add_edge(right)
        right.add_edge(left)

    def add_node(self, name: str) -> Cave:
        if name not in self:
            self[name] = Cave(name)
        return self[name]


InputType = CaveMap


# noinspection DuplicatedCode
def read_input() -> InputType:
    with open(Path(Path(__file__).parent, "input")) as f:
        return parse_input(f.read())


def parse_input(content: str) -> InputType:
    caves = CaveMap()
    [caves.add_edge(*row) for row in map(parse_row, content.split("\n"))]
    return caves


def parse_row(row: str) -> Tuple[str, str]:
    # noinspection PyTypeChecker
    return row.split("-")


def solve_1(values: InputType):
    print("Solve 1:", count_paths(values))


def count_paths(caves: CaveMap) -> int:
    return len(list(generate_cave_paths(caves, "start", "end")))


CavePath = namedtuple("CavePath", ["position", "path_till_here"])


def generate_cave_paths(caves: CaveMap, start: str, end: str) -> Iterator[Tuple[Cave]]:
    yield from generate_path(caves[start], caves[end])


def generate_path(start: Cave, end: Cave) -> Iterator[Tuple[Cave]]:
    target = end
    stack: LifoQueue[CavePath] = LifoQueue()
    stack.put(CavePath(start, tuple()))
    while not stack.empty():
        position, path_till_here = stack.get()
        new_path = path_till_here + (position,)
        if position == target:
            yield new_path
            continue

        for cave in position.edges:
            if cave.is_big() or cave not in path_till_here:
                stack.put(CavePath(cave, new_path))


def solve_2(values: InputType):
    print("Solve 2:", count_paths_twice(values))


def count_paths_twice(caves: CaveMap) -> int:
    return len(list(generate_cave_paths_twice(caves, "start", "end")))


CavePathTwice = namedtuple("CavePath", ["position", "path_till_here", "small_gone"])


def generate_cave_paths_twice(
    caves: CaveMap, start: str, end: str
) -> Iterator[Tuple[Cave]]:
    yield from generate_path_twice(caves[start], caves[end])


def generate_path_twice(start: Cave, end: Cave) -> Iterator[Tuple[Cave]]:
    target = end
    stack: LifoQueue[CavePathTwice] = LifoQueue()
    stack.put(CavePathTwice(start, tuple(), False))
    while not stack.empty():
        position, path_till_here, small_gone = stack.get()
        new_path = path_till_here + (position,)
        if position == target:
            yield new_path
            continue

        for cave in position.edges:
            if cave == start:
                continue
            if cave.is_big() or cave not in path_till_here:
                stack.put(CavePathTwice(cave, new_path, small_gone))
            elif not small_gone:
                stack.put(CavePathTwice(cave, new_path, True))


if __name__ == "__main__":
    input_values = read_input()
    print(input_values, sep="\n")
    solve_1(input_values)
    solve_2(input_values)
