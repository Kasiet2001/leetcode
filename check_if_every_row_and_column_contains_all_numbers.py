def checkValid(matrix):
    n = len(matrix)
    col = list(zip(*matrix))
    for i in range(n):
        if len(set(matrix[i])) != n or len(set(col[i])) != n:
            return False
    return True
print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))