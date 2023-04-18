def isPowerOfFour(n):
    from math import log
    return n > 0 and log(n, 3).is_integer()
print(isPowerOfFour(243))