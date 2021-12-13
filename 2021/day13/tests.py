from .challenge import *

base_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

base_paper, base_instructions = parse_input(base_input)


def test_can_count_empty():
    assert base_paper.fold(base_instructions[0]).count_empty() == 17
