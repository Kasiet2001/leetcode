def minFallingPathSum(matrix):
    m = float('inf')
    prev_row = [m] + matrix[0][:] + [m]
    for i in range(1, len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            temp.append(matrix[i][j] + min(prev_row[j: j + 3]))
        prev_row = [m] + temp + [m]
    return prev_row[1: 1 + 3]
print(minFallingPathSum([[-19,57],[-40,-5]]))