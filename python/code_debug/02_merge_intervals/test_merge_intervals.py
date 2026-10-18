import copy
import random

import pytest

from merge_intervals import merge


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),                       # touching
        ([[1, 10], [2, 3]], [[1, 10]]),                     # contained
        ([[8, 10], [1, 3], [2, 6]], [[1, 6], [8, 10]]),     # unsorted input
        ([], []),
        ([[5, 7]], [[5, 7]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3], [3, 5], [10, 12]], [[1, 5], [10, 12]]),
        ([[2, 3], [4, 5], [6, 7]], [[2, 3], [4, 5], [6, 7]]),   # nothing overlaps
        ([[1, 5], [1, 5]], [[1, 5]]),                       # exact duplicates
        ([[-5, -2], [-3, 0]], [[-5, 0]]),                   # negatives
    ],
)
def test_examples(intervals, expected):
    assert merge(intervals) == expected


def test_input_not_modified():
    data = [[1, 3], [2, 6], [8, 10]]
    snapshot = copy.deepcopy(data)
    merge(data)
    assert data == snapshot


def test_returns_new_lists_not_aliases():
    data = [[1, 2], [5, 6]]
    out = merge(data)
    out[0][0] = 99
    assert data == [[1, 2], [5, 6]]


def brute(intervals):
    points = set()
    for s, e in intervals:
        points.update(range(s * 2, e * 2 + 1))     # doubled coordinates so touching counts
    result, cur = [], None
    for p in sorted(points):
        if cur and p == cur[1] + 1:
            cur[1] = p
        elif cur is None or p > cur[1] + 1:
            if cur:
                result.append(cur)
            cur = [p, p]
        else:
            cur[1] = p
    if cur:
        result.append(cur)
    return [[a // 2, b // 2] for a, b in result]


def test_random_against_bruteforce():
    random.seed(2)
    for _ in range(300):
        n = random.randint(0, 8)
        intervals = []
        for _ in range(n):
            s = random.randint(0, 20)
            intervals.append([s, s + random.randint(0, 5)])
        assert merge(intervals) == brute(intervals), intervals
