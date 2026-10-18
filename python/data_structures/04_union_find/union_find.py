class UnionFind:
    def __init__(self, n: int):
        raise NotImplementedError

    def find(self, x: int) -> int:
        raise NotImplementedError

    def union(self, x: int, y: int) -> bool:
        """Merge sets. Return True if a merge happened, False if already connected."""
        raise NotImplementedError

    def connected(self, x: int, y: int) -> bool:
        raise NotImplementedError

    def size_of(self, x: int) -> int:
        raise NotImplementedError

    # also needs an attribute `count` = number of disjoint sets (starts at n)


def redundant_connection(edges: list[list[int]]) -> list[int]:
    """Return the edge that closes the cycle (nodes are labelled 1..n)."""
    raise NotImplementedError
