import pytest

from product_except_self import product_except_self


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([0, 0], [0, 0]),            # two zeros -> everything zero
        ([5, 0], [0, 5]),            # one zero -> only the zero slot is non-zero
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-2, -3, 4], [-12, -8, 6]),  # negatives
        ([0, 4, 0], [0, 0, 0]),
    ],
)
def test_cases(nums, expected):
    assert product_except_self(nums) == expected


def test_does_not_modify_input():
    nums = [1, 2, 3, 4]
    product_except_self(nums)
    assert nums == [1, 2, 3, 4]


def test_large_input_is_fast():
    nums = [1] * 100_000
    assert product_except_self(nums) == [1] * 100_000
