class MinHeap:
    def __init__(self):
        raise NotImplementedError

    def push(self, x) -> None:
        raise NotImplementedError

    def pop(self):
        """Remove and return the smallest item. Raise IndexError if empty."""
        raise NotImplementedError

    def peek(self):
        """Return the smallest item without removing it. Raise IndexError if empty."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    @classmethod
    def heapify(cls, items):
        """Build a heap from a list in O(n). Must not modify `items`."""
        raise NotImplementedError


def heap_sort(items):
    """Return a new ascending list using MinHeap."""
    raise NotImplementedError
