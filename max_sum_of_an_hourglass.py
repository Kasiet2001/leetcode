def maxSum(grid):
    m = len(grid)
    n = len(grid[0])
    ans = 0
    for i in range(m - 2):
        for j in range(n - 2):
            res = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] \
                            + grid[i + 1][j + 1] \
                            + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
            ans = max(ans, res)
    return ans
print(maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))