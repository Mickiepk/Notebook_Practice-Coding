import time

import pytest

from coin_change import coin_change


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([5], 5, 1),
        ([3, 7], 11, -1),
        ([1, 3, 4], 6, 2),                 # greedy would answer 3
        ([2, 5, 10, 1], 27, 4),
        ([186, 419, 83, 408], 6249, 20),
        ([7], 0, 0),                       # amount 0 is always 0
        ([5, 10], 3, -1),                  # every coin bigger than amount
        ([2, 4], 7, -1),                   # parity makes it impossible
    ],
)
def test_cases(coins, amount, expected):
    assert coin_change(coins, amount) == expected


def test_large_amount_is_fast():
    start = time.time()
    assert coin_change([1, 2, 5], 10_000) == 2000
    assert time.time() - start < 2, "too slow - plain recursion without memo?"
