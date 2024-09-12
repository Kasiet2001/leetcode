def matrixSumQueries(n, queries):
    row_total, col_total = n, n
    rows, cols = [-1] * n, [-1] * n
    ans = 0
    for mat, idx, d in queries[::-1]:
        if mat == 0 and rows[idx] == -1:
            ans += d * col_total
            row_total -= 1
            rows[idx] = d
        elif mat == 1 and cols[idx] == -1:
            ans += d * row_total
            col_total -= 1
            cols[idx] = d
    return ans
print(matrixSumQueries(3, [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]))