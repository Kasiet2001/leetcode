def minimumOperationsToWriteY(grid):
    freq = [0] * 3
    nums = [0] * 3
    n = len(grid)
    for r in grid:
        for c in r:
            freq[c] += 1
    l, r = 0, n - 1
    row = 0
    while l < r:
        nums[grid[row][l]] += 1
        nums[grid[row][r]] += 1
        freq[grid[row][l]] -= 1
        freq[grid[row][r]] -= 1
        row += 1
        l += 1
        r -= 1
    for i in range(row, n):
        nums[grid[i][n // 2]] += 1
        freq[grid[i][n // 2]] -= 1
    ans = float('inf')
    for i in range(3):
        for j in range(3):
            if i != j:
                y = sum(nums) - nums[i]
                x = sum(freq) - freq[j]
                ans = min(ans, y + x)
    return ans
print(minimumOperationsToWriteY([[2,1,1],[2,0,0],[2,2,1]]))