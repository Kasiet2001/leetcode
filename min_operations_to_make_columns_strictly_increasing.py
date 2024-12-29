def minimumOperations(grid):
    rows = len(grid)
    cols = len(grid[0])
    operations = 0

    for j in range(cols):
        for i in range(rows - 1):
            if grid[i + 1][j] <= grid[i][j]:
                increment = grid[i][j] - grid[i + 1][j] + 1
                operations += increment
                grid[i + 1][j] += increment

    return operations
print(minimumOperations([[3,2],[1,3],[3,4],[0,1]]))