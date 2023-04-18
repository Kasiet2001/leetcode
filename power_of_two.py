def isPowerOfTwo(n):
    while n % 2 == 0 and n > 1:
        n = n / 2
    return n == 1
print(isPowerOfTwo(3))