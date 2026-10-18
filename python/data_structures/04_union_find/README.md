# 04 - Union-Find (Disjoint Set Union)

**Difficulty:** Medium | **Topics:** graph, DSU, path compression, union by size | **Target:** ~O(alpha(n)) per operation

## Problem

Implement `UnionFind(n)` for elements `0 .. n-1`, then use it to solve a classic graph problem.

| Method                | Meaning                                                               |
|-----------------------|-----------------------------------------------------------------------|
| `find(x)`             | representative (root) of the set containing `x`                       |
| `union(x, y)`         | merge the two sets; return `True` if they were different, `False` if already together |
| `connected(x, y)`     | are `x` and `y` in the same set?                                      |
| `count`               | attribute: current number of separate sets                            |
| `size_of(x)`          | number of elements in the set containing `x`                          |

### Then solve: Redundant Connection

```python
redundant_connection(edges: list[list[int]]) -> list[int]
```

`edges` describes a graph that started as a tree on nodes `1..n` and had **one extra edge** added (so it contains exactly one cycle).
Return the extra edge. If several edges could be removed, return the one that appears **last** in `edges`.

```
edges = [[1,2],[1,3],[2,3]]  ->  [2,3]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]  ->  [1,4]
```

## Hints

<details><summary>Hint 1</summary>Start with `parent[i] = i`. `find` follows parents up to the root.</details>
<details><summary>Hint 2</summary>Path compression: after finding the root, point every node on the path straight to it. Union by size: attach the smaller tree under the bigger one.</details>
<details><summary>Hint 3</summary>Redundant connection: process edges in order; the first edge whose endpoints are already connected is the answer. Mind the 1-based node labels.</details>
<details><summary>Careful</summary>Deep chains: an iterative `find` is safer than a recursive one for 100,000 nodes.</details>

## Run the tests

```bash
cd python/data_structures/04_union_find
pytest -v
```
