def zigzagTraversal(grid):
    m, n = len(grid), len(grid[0])
    result = []
    skip = False

    for i in range(m):
        if i % 2 == 0:
            row_range = range(n)
        else:
            row_range = range(n - 1, -1, -1)

        for j in row_range:
            if skip:
                skip = False
                continue
            result.append(grid[i][j])
            skip = True

    return result
print(zigzagTraversal([[1,2,3],[4,5,6],[7,8,9]]))