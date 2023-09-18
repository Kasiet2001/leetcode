def kWeakestRows(mat, k):
    r = [(sum(row), i) for i, row in enumerate(mat)]
    rows = sorted(r, key=lambda x: x[0])
    return [rows[i][1] for i in range(k)]
print(kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))