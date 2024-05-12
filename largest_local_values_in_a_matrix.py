def largestLocal(grid):
    n = len(grid)
    res = [[0] * (n - 2) for _ in range(n - 2)]
    for i in range(n - 2):
        for j in range(n - 2):
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    res[i][j] = max(res[i][j], grid[r][c])
    return res
print(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))