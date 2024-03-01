def maximumOddBinaryNumber(s):
    ones = s.count('1')
    ans = ''
    for i in range(len(s) - 1):
        if ones > 1:
            ans += '1'
            ones -= 1
        else:
            ans += '0'
    return ans + '1'
print(maximumOddBinaryNumber("0101"))

