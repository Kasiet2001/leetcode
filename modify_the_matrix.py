def modifiedMatrix(matrix):
    columnMax = [max(col) for col in zip(*matrix)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                matrix[i][j] = columnMax[j]
    return matrix
print(modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))