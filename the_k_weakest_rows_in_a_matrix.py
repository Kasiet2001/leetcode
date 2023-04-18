def kWeakestRows(mat, k):
    rows = []
    m = sorted(mat)[:k]
    for i in range(k):
        for j in range(len(mat)):
            if m[i] == mat[j] and j not in rows and len(rows) != k:
                rows.append(j)
            else:
                continue
    return rows
print(kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))