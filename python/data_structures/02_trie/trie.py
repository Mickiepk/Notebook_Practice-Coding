class Trie:
    def __init__(self):
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError

    def words_with_prefix(self, prefix: str) -> list[str]:
        """All stored words starting with prefix, sorted alphabetically."""
        raise NotImplementedError

    def count_words(self) -> int:
        """Number of distinct words stored."""
        raise NotImplementedError
