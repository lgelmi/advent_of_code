from .challenge import *
from numpy.testing import assert_array_equal

base_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]
base_segments = list(map(Segment.from_str, base_input))
base_board = draw_board(base_segments)


def test_can_draw_horizontally():
    segment = base_segments[0]
    board = base_board.copy()
    segment.draw_horizontally_on_board(board)
    assert all(board[segment.start.y, segment.start.x : segment.start.x + 1] == 1)


def test_can_draw_vertically():
    segment = base_segments[4]
    board = base_board.copy()
    segment.draw_vertically_on_board(board)
    assert all(board[segment.start.y : segment.start.y + 1, 7] == 1)


def test_can_draw():
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]
    board = base_board.copy()
    draw_segments_on_board(base_segments, board)
    assert_array_equal(board, expected)


def test_can_count_points():
    assert get_dangerous_point_count(base_segments) == 5


def test_can_draw_diagonally():
    expected = [
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
        [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
        [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]
    board = base_board.copy()
    draw_segments_on_board(base_segments, board, True)
    assert_array_equal(board, expected)


def test_can_count_points_diagonally():
    assert get_dangerous_point_count_diagonal(base_segments) == 12
