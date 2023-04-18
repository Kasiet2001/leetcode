def kthSmallest(matrix, k):
    m = []
    for i in matrix:
        m.extend(i)
    return sorted(m)[k - 1]
print(kthSmallest([[-5]], 1))