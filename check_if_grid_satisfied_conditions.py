def satisfiesConditions(grid):
    m = len(grid)
    n = len(grid[0])
    if m == 1:
        for j in range(n - 1):
            if grid[0][j] == grid[0][j + 1]:
                return False
        return True

    for i in range(m - 1):
        for j in range(n):

            if grid[i][j] != grid[i + 1][j]:
                return False

            if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                return False

    return True
print(satisfiesConditions([[1],[2],[3]]))