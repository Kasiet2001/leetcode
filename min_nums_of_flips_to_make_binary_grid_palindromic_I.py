def minFlips(grid):
    row_res = 0
    col_res = 0
    cols = list(zip(*grid))
    for row in grid:
        for l in range(len(row) // 2):
            r = len(row) - 1 - l
            if row[l] != row[r]:
                row_res += 1
    for col in cols:
        for l in range(len(col) // 2):
            r = len(col) - 1 - l
            if col[l] != col[r]:
                col_res += 1
    return min(row_res, col_res)
print(minFlips([[1],[0]]))