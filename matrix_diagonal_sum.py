def diagonalSum(mat):
    n = len(mat)
    ans = 0
    for i in range(n):
        ans += mat[i][i] + mat[i][n - i - 1]
    if n % 2 == 1:
        ans -= mat[n // 2][n // 2]
    return ans
print(diagonalSum([[1,2,3], [4,5,6], [7,8,9]]))