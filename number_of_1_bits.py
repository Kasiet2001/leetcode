def hammingWeight(n):
    return bin(n)[2:].count('1')
print(hammingWeight(1011))