def maxMatrixSum(matrix):
    total_sum = 0
    neg = 0
    min_abs_val = float('inf')
    for row in matrix:
        for val in row:
            total_sum += abs(val)
            if val < 0:
                neg += 1
            min_abs_val = min(min_abs_val, abs(val))
    if neg % 2 != 0:
        total_sum -= 2 * min_abs_val
    return total_sum
print(maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))