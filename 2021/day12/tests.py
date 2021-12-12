from .challenge import *

base_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
base_caves = parse_input(base_input)
medium_input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
medium_caves = parse_input(medium_input)


def test_can_count_paths():
    assert count_paths(base_caves) == 10
    assert count_paths(medium_caves) == 19


def test_can_count_paths_twice():
    assert count_paths_twice(base_caves) == 36
    assert count_paths_twice(medium_caves) == 103
