def maxProduct(n):
    digits = [int(i) for i in str(n)]
    digits.sort()
    return digits[-2] * digits[-1]
print(maxProduct(31))