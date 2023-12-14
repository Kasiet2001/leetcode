def onesMinusZeros(grid):
    ans = []
    ones_col = list(sum(i) for i in zip(*grid))
    for row in grid:
        diff = []
        ones_row = sum(row)
        zeros_row = len(row) - ones_row
        for j in range(len(row)):
            diff.append(ones_row + ones_col[j] - zeros_row - (len(grid) - ones_col[j]))
        ans.append(diff)
    return ans
print(onesMinusZeros([[1,1,1],[1,1,1]]))