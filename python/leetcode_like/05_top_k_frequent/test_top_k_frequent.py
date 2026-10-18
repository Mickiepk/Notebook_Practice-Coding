import random

import pytest

from top_k_frequent import top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 5, 5, 6, 6, 6, 6], 1, {6}),
        ([-1, -1, -2, -2, -2, 3], 2, {-1, -2}),   # negatives
        ([1, 2, 3], 3, {1, 2, 3}),                # k == number of distinct values
        ([7, 7, 7, 7], 1, {7}),                   # one distinct value
        ([0, 0, 0, 1, 1, 2], 1, {0}),             # zero is a valid element
    ],
)
def test_cases(nums, k, expected):
    result = top_k_frequent(nums, k)
    assert len(result) == k
    assert set(result) == expected


def test_no_duplicates_in_result():
    result = top_k_frequent([1, 1, 2, 2, 3, 3, 3], 3)
    assert len(result) == len(set(result))


def test_large_input():
    random.seed(1)
    nums = [random.randint(0, 50) for _ in range(100_000)]
    nums += [999] * 5000  # clearly the most frequent
    assert 999 in top_k_frequent(nums, 1)
