def bfs(x, y, grid, visited):
    rows, columns = len(grid), len(grid[0])
    queue = [(x, y)]
    visited.add((x, y))

    while queue:
        x, y = queue.pop(0)
        directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

        for i, j in directions:
            x2, y2 = x + i, y + j
            if ((0 <= x2 < rows) and
                    (0 <= y2 < columns) and
                    grid[x2][y2] == 1 and (x2, y2) not in visited):
                queue.append((x2, y2))
                visited.add((x2, y2))


def num_of_island(grid):
    rows, columns = len(grid), len(grid[0])
    islands = 0
    visited = set()

    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == 1 and (x, y) not in visited:
                bfs(x, y, grid, visited)
                islands += 1
    return islands


grid = [
    [0, 0, 0, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]

print(f"Кількість островів: {num_of_island(grid)}")
