import copy

import pytest

from number_of_islands import num_islands


def g(rows):
    return [list(r) for r in rows]


@pytest.mark.parametrize(
    "rows, expected",
    [
        (["1100", "1001", "0011"], 2),
        (["11110", "11010", "11000", "00000"], 1),
        (["11000", "11000", "00100", "00011"], 3),
        (["101", "010", "101"], 5),     # diagonals do NOT connect
        (["1"], 1),
        (["0"], 0),
        (["000", "000"], 0),
        (["111", "111", "111"], 1),
        (["1", "0", "1", "1"], 2),      # single column
        (["10101"], 3),                 # single row
        ([], 0),                        # empty grid
    ],
)
def test_cases(rows, expected):
    grid = g(rows)
    assert num_islands(copy.deepcopy(grid)) == expected


def test_empty_rows():
    assert num_islands([[]]) == 0


def test_huge_single_island_no_recursion_error():
    grid = [["1"] * 300 for _ in range(300)]
    assert num_islands(grid) == 1


def test_snake_shaped_island():
    # a long winding island forces deep traversal
    n = 101
    grid = [["0"] * n for _ in range(n)]
    for r in range(0, n, 2):
        for c in range(n):
            grid[r][c] = "1"
    for r in range(1, n, 4):
        grid[r][n - 1] = "1"
    for r in range(3, n, 4):
        grid[r][0] = "1"
    assert num_islands(grid) == 1
