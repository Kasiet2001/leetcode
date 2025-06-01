def minAbsDiff(grid, k):
    m, n = len(grid), len(grid[0])
    ans = []

    for i in range(m - k + 1):
        row = []
        for j in range(n - k + 1):
            values = []
            for x in range(i, i + k):
                for y in range(j, j + k):
                    values.append(grid[x][y])

            values.sort()
            min_diff = float('inf')
            for a in range(1, len(values)):
                if values[a] != values[a - 1]:
                    min_diff = min(min_diff, abs(values[a] - values[a - 1]))

            row.append(min_diff if min_diff != float('inf') else 0)
        ans.append(row)

    return ans
print(minAbsDiff([[1,-2,3],[2,3,5]], 2))
