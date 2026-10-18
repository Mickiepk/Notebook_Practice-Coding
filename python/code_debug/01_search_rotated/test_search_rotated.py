import random

import pytest

from search_rotated import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([], 5, -1),
        ([3, 1], 1, 1),
        ([3, 1], 3, 0),
        ([5, 1, 3], 3, 2),
        ([5, 1, 3], 5, 0),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),   # target is the first element
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),   # target is the last element
        ([1, 2, 3, 4, 5], 4, 3),         # not rotated at all
        ([2, 3, 4, 5, 1], 1, 4),         # pivot at the end
    ],
)
def test_examples(nums, target, expected):
    assert search(nums, target) == expected


def test_missing_in_single_element_list():
    assert search([1], 2) == -1


def test_exhaustive_small_lists():
    for n in range(0, 9):
        base = list(range(0, n * 2, 2))          # distinct sorted values
        for r in range(max(n, 1)):
            nums = base[r:] + base[:r]
            for target in range(-1, n * 2 + 1):
                expected = nums.index(target) if target in nums else -1
                assert search(nums, target) == expected, (nums, target)


def test_random_large():
    random.seed(11)
    base = sorted(random.sample(range(10_000), 2000))
    r = 777
    nums = base[r:] + base[:r]
    for _ in range(500):
        t = random.randint(-5, 10_005)
        expected = nums.index(t) if t in nums else -1
        assert search(nums, t) == expected
