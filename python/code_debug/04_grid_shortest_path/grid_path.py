from collections import deque


def shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return -1
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    er, ec = end
    if grid[er][ec] == 1:
        return -1
    queue = deque([(sr, sc, 0)])
    visited = {(sr, sc)}
    while queue:
        r, c, dist = queue.pop()
        if (r, c) == (er, ec):
            return dist + 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc <= cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1
