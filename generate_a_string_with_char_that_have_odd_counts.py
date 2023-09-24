def generateTheString(n):
    if n % 2:
        return 'a' * n
    return 'a' * (n - 1) + 'b'
print(generateTheString(8))