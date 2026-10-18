# Spoiler - bugs in `grid_path.py`

There are 4 planted bugs.

## Bug 1

`pop()` takes from the right end, which turns the BFS queue into a DFS stack. The first path found is not the shortest.

```diff
- r, c, dist = queue.pop()
+ r, c, dist = queue.popleft()
```

## Bug 2

Off-by-one on the column bound: `nc == cols` passes the check and `grid[nr][nc]` raises `IndexError` at the right edge.

```diff
- 0 <= nc <= cols
+ 0 <= nc < cols
```

## Bug 3

Only the end cell is checked. A start that is a wall must also return -1.

```diff
- if grid[er][ec] == 1:
+ if grid[sr][sc] == 1 or grid[er][ec] == 1:
```

## Bug 4

Returns the number of cells on the path instead of the number of steps (`start == end` should be 0).

```diff
- return dist + 1
+ return dist
```
