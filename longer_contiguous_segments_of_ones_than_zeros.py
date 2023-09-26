def checkZeroOnes(s):
    ones = zeros = 0
    curr_ones = curr_zeros = 0
    for i in s:
        if i == 1:
            curr_ones += 1
            curr_zeros = 0
        else:
            curr_ones = 0
            curr_zeros += 1
        ones = max(curr_ones, ones)
        zeros = max(curr_zeros, zeros)
    return ones > zeros
print(checkZeroOnes("1101"))

