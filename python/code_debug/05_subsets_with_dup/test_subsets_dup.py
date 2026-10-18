import itertools
import random

import pytest

from subsets_dup import subsets_with_dup


def norm(result):
    return sorted(tuple(sorted(s)) for s in result)


def brute(nums):
    seen = set()
    for r in range(len(nums) + 1):
        for c in itertools.combinations(nums, r):
            seen.add(tuple(sorted(c)))
    return sorted(seen)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
        ([0], [[], [0]]),
        ([], [[]]),
        ([2, 1, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),     # unsorted input
        ([1, 1, 1], [[], [1], [1, 1], [1, 1, 1]]),
        ([4, 4, 4, 1, 4], None),
    ],
)
def test_examples(nums, expected):
    expected = brute(nums) if expected is None else norm(expected)
    assert norm(subsets_with_dup(nums)) == expected


def test_subsets_are_independent_lists():
    out = subsets_with_dup([1, 2])
    assert len(out) == 4
    assert sum(len(s) for s in out) == 4   # [], [1], [2], [1,2]


def test_no_duplicate_subsets():
    out = [tuple(sorted(s)) for s in subsets_with_dup([1, 2, 2, 3, 3])]
    assert len(out) == len(set(out))


def test_input_not_modified():
    data = [3, 1, 3, 2]
    snapshot = list(data)
    subsets_with_dup(data)
    assert data == snapshot


def test_distinct_values_give_power_set():
    assert len(subsets_with_dup(list(range(10)))) == 2 ** 10


def test_random_against_bruteforce():
    random.seed(8)
    for _ in range(150):
        nums = [random.randint(0, 3) for _ in range(random.randint(0, 7))]
        assert norm(subsets_with_dup(nums)) == brute(nums), nums
