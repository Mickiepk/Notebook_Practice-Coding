# 01 - LRU Cache

**Difficulty:** Medium | **Topics:** hash map + doubly linked list | **Target:** O(1) `get` and `put`

## Problem

Design a cache with a fixed `capacity` that evicts the **Least Recently Used** item when it is full.

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)      # 1
cache.put(3, 3)   # evicts key 2 (1 was used more recently)
cache.get(2)      # -1
```

- `get(key)` returns the value, or `-1` if missing. A successful `get` makes the key **most recently used**.
- `put(key, value)` inserts or updates. Updating also makes it most recently used. If the insert exceeds capacity, evict the least recently used key.
- Both operations must be **O(1)**.

## Constraints

- `1 <= capacity <= 3000`, keys and values are ints.

## Hints

<details><summary>Hint 1</summary>A dict gives O(1) lookup. A doubly linked list gives O(1) "move to front" and "remove from back".</details>
<details><summary>Hint 2</summary>Use two dummy nodes (head and tail) so you never special-case an empty list.</details>
<details><summary>Careful</summary>`put` on an existing key must NOT evict anything, and must refresh recency.</details>

## Challenge

Do **not** use `collections.OrderedDict`. Build the linked list yourself (that is the interview question).

## Run the tests

```bash
cd python/data_structures/01_lru_cache
pytest -v
```
