import copy
import itertools
import random

import pytest

from three_sum import three_sum


def norm(result):
    return sorted(sorted(t) for t in result)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([0], []),
        ([0, 0], []),
        ([-2, 1, 4], []),                          # must not reuse an element
        ([-2, 0, 0, 0, 2, 2, 2], [[-2, 0, 2], [0, 0, 0]]),  # many duplicates -> no repeated triplets
        ([-2, 0, 2, -2], [[-2, 0, 2]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
        ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ],
)
def test_examples(nums, expected):
    assert norm(three_sum(nums)) == norm(expected)


def test_no_duplicate_triplets():
    result = three_sum([-1, -1, -1, 0, 0, 1, 1, 2, 2])
    as_tuples = [tuple(t) for t in result]
    assert len(as_tuples) == len(set(as_tuples))


def test_input_not_modified():
    data = [3, -1, 2, -2, 0]
    snapshot = list(data)
    three_sum(data)
    assert data == snapshot


def test_random_against_bruteforce():
    random.seed(4)
    for _ in range(300):
        nums = [random.randint(-5, 5) for _ in range(random.randint(0, 9))]
        expected = {tuple(sorted(c)) for c in itertools.combinations(nums, 3) if sum(c) == 0}
        got = [tuple(sorted(t)) for t in three_sum(copy.copy(nums))]
        assert len(got) == len(set(got)), nums
        assert set(got) == expected, nums
