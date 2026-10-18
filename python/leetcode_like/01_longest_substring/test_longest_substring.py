import time

import pytest

from longest_substring import length_of_longest_substring


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),       # answer starts after the first repeat, not at index 0
        ("abba", 2),       # left pointer must never move backwards
        ("tmmzuxt", 5),    # same trap, longer
        ("a b a", 3),      # space counts as a character
        ("abcdefg", 7),    # no repeats at all
    ],
)
def test_examples_and_edge_cases(s, expected):
    assert length_of_longest_substring(s) == expected


def test_large_input_is_fast():
    s = "".join(chr(97 + i % 26) for i in range(300_000))
    start = time.time()
    assert length_of_longest_substring(s) == 26
    assert time.time() - start < 2, "too slow - aim for O(n)"
