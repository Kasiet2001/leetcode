def firstCompleteIndex(arr, mat):
    m = len(mat)
    n = len(mat[0])
    map = {}
    for i in range(m):
        for j in range(n):
            map[mat[i][j]] = [i, j]
    row = [0] * m
    col = [0] * n
    for i in range(len(arr)):
        x = map[arr[i]]
        row[x[0]] += 1
        col[x[1]] += 1
        if row[x[0]] == n or col[x[1]] == m:
            return i
    return -1
print(firstCompleteIndex([6,2,3,1,4,5], [[5,1],[2,4],[6,3]]))