def canPartitionGrid(grid):
    rows_sum = sum(sum(i) for i in grid)
    cols = list(zip(*grid))
    cols_sum = sum(sum(i) for i in cols)
    c = 0
    r = 0
    for i in range(len(grid)):
        rows_sum -= sum(grid[i])
        r += sum(grid[i])
        if r == rows_sum:
            return True
    for i in range(len(cols)):
        cols_sum -= sum(cols[i])
        c += sum(cols[i])
        if c == cols_sum:
            return True
    return False
print(canPartitionGrid([[54756,54756]]))