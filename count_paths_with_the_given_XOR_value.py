from functools import lru_cache
def countPathsWithXorValue(grid, k):
    MOD = 10 ** 9 + 7
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def dp(i, j, xor_value):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1 if (xor_value ^ grid[i][j]) == k else 0
        new_xor = xor_value ^ grid[i][j]
        right = dp(i, j + 1, new_xor)
        down = dp(i + 1, j, new_xor)

        return (right + down) % MOD
    return dp(0, 0, 0)
print(countPathsWithXorValue([[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], 2))
