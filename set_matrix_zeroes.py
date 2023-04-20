def setZeroes(matrix):
    m = []
    n = []
    for i in zip(*matrix):
        if 0 in i:
            m.append([0] * len(i))
        else:
            m.append(i)
    for i in zip(*m):
        n.append(i)
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            if matrix[j][k] == 0:
                n[j] = [0] * len(matrix[j])
    matrix[:] = n
    return matrix
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
