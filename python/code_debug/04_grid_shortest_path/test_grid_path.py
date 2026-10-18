import pytest

from grid_path import shortest_path

OPEN3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_same_cell():
    assert shortest_path(OPEN3, (1, 1), (1, 1)) == 0


def test_straight_line():
    assert shortest_path([[0, 0, 0, 0]], (0, 0), (0, 3)) == 3


def test_open_grid_corner_to_corner():
    assert shortest_path(OPEN3, (0, 0), (2, 2)) == 4


def test_detour_around_wall():
    grid = [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]]
    assert shortest_path(grid, (0, 0), (2, 0)) == 6


def test_no_path():
    grid = [[0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]]
    assert shortest_path(grid, (0, 0), (2, 2)) == -1


def test_start_is_wall():
    grid = [[1, 0], [0, 0]]
    assert shortest_path(grid, (0, 0), (1, 1)) == -1


def test_end_is_wall():
    grid = [[0, 0], [0, 1]]
    assert shortest_path(grid, (0, 0), (1, 1)) == -1


def test_empty_grids():
    assert shortest_path([], (0, 0), (0, 0)) == -1
    assert shortest_path([[]], (0, 0), (0, 0)) == -1


def test_must_pick_shorter_of_two_routes():
    grid = [[0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]]
    # short way: down the left column then along the bottom row = 8 steps
    assert shortest_path(grid, (0, 0), (4, 4)) == 8


def test_right_edge_and_bottom_edge_are_reachable():
    grid = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    assert shortest_path(grid, (0, 2), (2, 2)) == 2
    assert shortest_path(grid, (2, 0), (0, 2)) == 4


def test_big_open_grid():
    n = 60
    grid = [[0] * n for _ in range(n)]
    assert shortest_path(grid, (0, 0), (n - 1, n - 1)) == 2 * (n - 1)


def test_spiral_maze():
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    assert shortest_path(grid, (0, 0), (4, 4)) == 16
