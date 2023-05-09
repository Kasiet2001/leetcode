def spiralOrder(matrix):
    if not matrix:
        return []
    ans = []
    rows, cols = len(matrix), len(matrix[0])
    t, b, l, r = 0, rows - 1, 0, cols - 1
    while len(ans) < rows * cols:
        for i in range(l, r + 1):
            ans.append(matrix[t][i])
        t += 1
        for i in range(t, b + 1):
            ans.append(matrix[i][r])
        r -= 1
        if t <= b:
            for i in range(r, l - 1, -1):
                ans.append(matrix[b][i])
            b -= 1
        if l <= r:
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
    return ans
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))