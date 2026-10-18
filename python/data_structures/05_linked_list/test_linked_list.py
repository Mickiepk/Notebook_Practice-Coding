import pytest

from linked_list import add_two_numbers, from_list, reverse_between, to_list


# ---- Part A -----------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),  # final carry node
        ([5], [5], [0, 1]),                                              # carry only at the end
        ([1, 8], [0], [1, 8]),                                           # adding zero
        ([9, 9], [1], [0, 0, 1]),                                        # carry ripples through longer list
        ([1], [9, 9, 9], [0, 0, 0, 1]),                                  # first list shorter
        ([3, 4, 2], [4, 6, 5], [7, 0, 8]),
    ],
)
def test_add_two_numbers(a, b, expected):
    assert to_list(add_two_numbers(from_list(a), from_list(b))) == expected


def test_add_does_not_destroy_inputs():
    l1, l2 = from_list([2, 4, 3]), from_list([5, 6, 4])
    add_two_numbers(l1, l2)
    assert to_list(l1) == [2, 4, 3]
    assert to_list(l2) == [5, 6, 4]


def test_add_long_lists():
    a = [9] * 100
    out = to_list(add_two_numbers(from_list(a), from_list([1])))
    assert out == [0] * 100 + [1]


# ---- Part B -----------------------------------------------------------
@pytest.mark.parametrize(
    "values, left, right, expected",
    [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([3, 5], 1, 2, [5, 3]),                    # whole list
        ([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5]),  # starts at head
        ([1, 2, 3, 4, 5], 3, 5, [1, 2, 5, 4, 3]),  # ends at tail
        ([1, 2, 3, 4, 5], 3, 3, [1, 2, 3, 4, 5]),  # left == right, nothing changes
        ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
        ([1, 2], 2, 2, [1, 2]),
    ],
)
def test_reverse_between(values, left, right, expected):
    assert to_list(reverse_between(from_list(values), left, right)) == expected


def test_reverse_between_long():
    values = list(range(1, 1001))
    out = to_list(reverse_between(from_list(values), 10, 990))
    assert out == values[:9] + values[9:990][::-1] + values[990:]
