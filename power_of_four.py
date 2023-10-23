def isPowerOfFour(n):
    if n == 1:
        return True
    if n <= 0:
        return False

    while n > 1:
        if n % 4 != 0:
            return False
        n //= 4
    return True
print(isPowerOfFour(243))