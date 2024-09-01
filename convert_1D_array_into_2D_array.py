def construct2DArray(original, m, n):
    ans = []
    if m * n == len(original):
        row = []
        for i in range(m * n):
            row.append(original[i])
            if len(row) == n:
                ans.append(row)
                row = []
    return ans
print(construct2DArray([1,2], 1, 1))

