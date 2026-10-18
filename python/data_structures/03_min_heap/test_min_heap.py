import heapq
import random

import pytest

from min_heap import MinHeap, heap_sort


def drain(h):
    out = []
    while len(h):
        out.append(h.pop())
    return out


def test_push_pop_order():
    h = MinHeap()
    for x in [5, 3, 8, 1, 9, 2]:
        h.push(x)
    assert len(h) == 6
    assert h.peek() == 1
    assert drain(h) == [1, 2, 3, 5, 8, 9]


def test_empty_errors():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.pop()
    with pytest.raises(IndexError):
        h.peek()


def test_single_element():
    h = MinHeap()
    h.push(7)
    assert h.pop() == 7
    assert len(h) == 0
    with pytest.raises(IndexError):
        h.pop()


def test_duplicates_and_negatives():
    h = MinHeap()
    for x in [3, 3, -1, -1, 0, 3]:
        h.push(x)
    assert drain(h) == [-1, -1, 0, 3, 3, 3]


def test_peek_does_not_remove():
    h = MinHeap()
    h.push(2)
    h.push(1)
    assert h.peek() == 1
    assert h.peek() == 1
    assert len(h) == 2


def test_interleaved_push_pop_matches_heapq():
    random.seed(7)
    mine, ref = MinHeap(), []
    for _ in range(5000):
        if ref and random.random() < 0.4:
            assert mine.pop() == heapq.heappop(ref)
        else:
            x = random.randint(-100, 100)
            mine.push(x)
            heapq.heappush(ref, x)
        assert len(mine) == len(ref)
        if ref:
            assert mine.peek() == ref[0]


def test_heapify_basic_and_no_mutation():
    data = [9, 4, 7, 1, 8, 2, 6]
    snapshot = list(data)
    h = MinHeap.heapify(data)
    assert data == snapshot
    assert len(h) == 7
    assert drain(h) == sorted(snapshot)


def test_heapify_small_inputs():
    assert len(MinHeap.heapify([])) == 0
    h = MinHeap.heapify([4])
    assert h.pop() == 4
    h = MinHeap.heapify([2, 1])     # root has only a left child
    assert drain(h) == [1, 2]


def test_heapify_random():
    random.seed(3)
    data = [random.randint(-1000, 1000) for _ in range(2000)]
    assert drain(MinHeap.heapify(data)) == sorted(data)


def test_heap_sort():
    random.seed(5)
    data = [random.randint(0, 50) for _ in range(500)]
    assert heap_sort(data) == sorted(data)
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]
