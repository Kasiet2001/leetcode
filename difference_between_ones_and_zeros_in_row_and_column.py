def onesMinusZeros(grid):
    ones_row = [0] * len(grid)
    ones_col = [0] * len(grid[0])
    for i in range(len(ones_row)):
        for j in range(len(ones_col)):
            if grid[i][j]:
                ones_row[i] += 1
                ones_col[j] += 1
            else:
                ones_row[i] -= 1
                ones_col[j] -= 1
    ans = []
    for m in range(len(grid)):
        r = [0] * len(grid[0])
        for n in range(len(grid[0])):
            r[n] = ones_row[m] + ones_col[n]
        ans.append(r)
    return ans
print(onesMinusZeros([[1,1,1],[1,1,1]]))