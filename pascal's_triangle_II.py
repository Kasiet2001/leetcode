def getRow(rowIndex):
    rows = [[] for _ in range(rowIndex + 1)]
    rows[0].append(1)
    for i in range(1, rowIndex + 1):
        rows[i].append(1)
        for j in range(1, len(rows[i - 1])):
            rows[i].append(rows[i - 1][j - 1] + rows[i - 1][j])
        rows[i].append(1)
    return rows[rowIndex]
print(getRow(3))