def rotate(matrix):
    matrix = matrix[::-1]
    matrix[:] = zip(*matrix)
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
