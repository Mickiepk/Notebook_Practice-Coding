class LRUCache:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: int) -> int:
        """Return value for key or -1. Marks key as most recently used."""
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        """Insert/update key. Evict the least recently used key if over capacity."""
        raise NotImplementedError
