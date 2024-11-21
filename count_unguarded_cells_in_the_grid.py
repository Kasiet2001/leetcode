def countUnguarded(m, n, guards, walls):
    grid = [[0] * n for _ in range(m)]
    for x, y in guards + walls:
        grid[x][y] = 2
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for gx, gy in guards:
        for dx, dy in directions:
            x, y = gx, gy
            while 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] != 2:
                x += dx
                y += dy
                grid[x][y] = 1
    return sum(row.count(0) for row in grid)
print(countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))

