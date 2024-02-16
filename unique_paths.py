def uniquePaths(m, n):
    table = []
    for i in range(m):
        table.append([0] * n)
    table[0][0] = 1
    for i in range(m):
        for j in range(n):
            current = table[i][j]
            if j + 1 < n:
                table[i][j + 1] += current
            if i + 1 < m:
                table[i + 1][j] += current
    return table[-1][-1]
print(uniquePaths(3, 2))