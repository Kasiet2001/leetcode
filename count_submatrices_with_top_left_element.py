def countSubmatrices(grid, k):
    ans = 0
    row = len(grid)
    column = len(grid[0])
    prev_sum = [0] * column
    for i in range(row):
        curr = 0
        for j in range(column):
            curr += grid[i][j]
            prev_sum[j] += curr
            if prev_sum[j] <= k:
                ans += 1
            else:
                break
    return ans
print(countSubmatrices([[7,6,3],[6,6,1]], 18))