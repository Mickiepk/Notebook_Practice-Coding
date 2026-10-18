# 04 - Number of Islands

**Difficulty:** Medium | **Topics:** graph, DFS / BFS, grid | **Target:** O(rows * cols)

## Problem

You get a 2D grid of `"1"` (land) and `"0"` (water), stored as **strings**.
Return the number of islands. An island is a group of `"1"` cells connected **horizontally or vertically** (not diagonally).

## Examples

```
["1","1","0","0"]
["1","0","0","1"]      -> 2 islands
["0","0","1","1"]
```

```
[["1","0","1"],
 ["0","1","0"],       -> 5 islands (diagonals do not connect)
 ["1","0","1"]]
```

## Constraints

- `0 <= rows, cols <= 300` (an empty grid is possible)
- You may mutate the grid you are given (the tests pass a fresh copy every time).

## Hints

<details><summary>Hint 1</summary>Scan every cell. When you find an unvisited `"1"`, count one island and flood-fill everything connected to it.</details>
<details><summary>Hint 2</summary>Mark visited cells (mutate the grid or use a set) so you never count the same island twice.</details>
<details><summary>Careful</summary>A 300x300 grid of all land is one island of 90,000 cells. Python's recursion limit is ~1000. What do you use instead of recursion?</details>

## Run the tests

```bash
cd python/leetcode_like/04_number_of_islands
pytest -v
```
