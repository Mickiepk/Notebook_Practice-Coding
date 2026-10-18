# Debug 04 - Shortest Path in a Grid (BFS)

**Difficulty:** Medium | **Topics:** BFS, graph, grid

## The problem the code is supposed to solve

`grid[r][c]` is `0` (open) or `1` (wall). You can move up, down, left or right (no diagonals).

`shortest_path(grid, start, end)` returns the **minimum number of steps** from `start=(row, col)` to `end=(row, col)`, or `-1` if there is no path.

- `start == end` (on an open cell) -> `0` steps.
- If `start` or `end` is a wall -> `-1`.
- Empty grid -> `-1`.

```
grid = [[0,0,0],
        [1,1,0],
        [0,0,0]]
shortest_path(grid, (0,0), (2,0))  ->  6
```

## How to practice

1. **Read** `grid_path.py` without running anything. It looks reasonable, but it is wrong.
2. Write your findings in a copy of `../REVIEW_TEMPLATE.md` (line number, what is wrong, an input that breaks it).
3. **Run** `pytest -v` to confirm which of your guesses were real.
4. **Fix** the code until every test passes.
5. Only then open `SPOILER_answer.md` and compare.

```bash
cd python/code_debug/04_grid_shortest_path
pytest -v
```
