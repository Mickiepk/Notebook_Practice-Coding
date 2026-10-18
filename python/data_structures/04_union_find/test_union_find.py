from union_find import UnionFind, redundant_connection


def test_initial_state():
    uf = UnionFind(5)
    assert uf.count == 5
    assert all(uf.find(i) == i for i in range(5))
    assert not uf.connected(0, 1)
    assert uf.size_of(3) == 1


def test_union_and_connected():
    uf = UnionFind(6)
    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.connected(0, 2)
    assert not uf.connected(0, 3)
    assert uf.count == 4
    assert uf.size_of(2) == 3


def test_union_same_set_returns_false_and_keeps_count():
    uf = UnionFind(3)
    uf.union(0, 1)
    assert uf.union(1, 0) is False
    assert uf.union(0, 0) is False
    assert uf.count == 2


def test_transitive_merge_of_two_groups():
    uf = UnionFind(8)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(1, 2)
    uf.union(5, 6)
    assert uf.connected(0, 3)
    assert not uf.connected(0, 4)
    uf.union(3, 4)
    assert uf.connected(0, 6)
    assert uf.count == 2      # {0..6} and {7}
    assert uf.size_of(0) == 7
    assert uf.size_of(7) == 1


def test_long_chain_no_recursion_error():
    n = 100_000
    uf = UnionFind(n)
    for i in range(n - 1):
        uf.union(i, i + 1)
    assert uf.count == 1
    assert uf.connected(0, n - 1)
    assert uf.size_of(0) == n


def test_single_element():
    uf = UnionFind(1)
    assert uf.count == 1
    assert uf.find(0) == 0


def test_redundant_connection_examples():
    assert redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


def test_redundant_connection_returns_last_candidate():
    # cycle 1-2-3-1: any of the three edges could be removed, the last one in the list is expected
    assert redundant_connection([[1, 2], [2, 3], [3, 1]]) == [3, 1]
    assert redundant_connection([[3, 1], [2, 3], [1, 2]]) == [1, 2]


def test_redundant_connection_extra_edge_late():
    edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]
    assert redundant_connection(edges) == [7, 1]


def test_redundant_connection_large():
    n = 50_000
    edges = [[i, i + 1] for i in range(1, n)] + [[1, n]]
    assert redundant_connection(edges) == [1, n]
