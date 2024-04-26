def minFallingPathSum(grid):
    n = len(grid)
    dp = grid[0]
    for row in range(1, n):
        next_dp = [float('inf')] * n
        for curr_c in range(n):
            for prev_c in range(n):
                if curr_c != prev_c:
                    next_dp[curr_c] = min(next_dp[curr_c], grid[row][curr_c] + dp[prev_c])
        dp = next_dp
    return min(dp)
print(minFallingPathSum([[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]))
