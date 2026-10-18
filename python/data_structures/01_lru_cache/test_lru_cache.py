from lru_cache import LRUCache


def test_leetcode_example():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)          # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)          # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


def test_missing_key():
    assert LRUCache(1).get(42) == -1


def test_capacity_one():
    c = LRUCache(1)
    c.put(1, 10)
    c.put(2, 20)
    assert c.get(1) == -1
    assert c.get(2) == 20


def test_update_existing_key_does_not_evict():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 100)        # update, cache still has 1 and 2
    assert c.get(2) == 2
    assert c.get(1) == 100


def test_update_refreshes_recency():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 99)         # 1 is now most recent, 2 is LRU
    c.put(3, 3)          # must evict 2
    assert c.get(2) == -1
    assert c.get(1) == 99
    assert c.get(3) == 3


def test_get_refreshes_recency():
    c = LRUCache(3)
    for k in (1, 2, 3):
        c.put(k, k)
    c.get(1)             # order now: 2 (LRU), 3, 1
    c.put(4, 4)          # evicts 2
    assert c.get(2) == -1
    assert {c.get(1), c.get(3), c.get(4)} == {1, 3, 4}


def test_value_zero_is_not_missing():
    c = LRUCache(2)
    c.put(1, 0)
    assert c.get(1) == 0


def test_many_operations():
    c = LRUCache(1000)
    for i in range(100_000):
        c.put(i, i)
    assert c.get(0) == -1
    assert c.get(99_999) == 99_999
    assert c.get(99_000) == 99_000
    assert c.get(98_999) == -1
