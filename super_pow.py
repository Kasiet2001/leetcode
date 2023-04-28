def superPow(a, b):
    b = int(''.join(map(str, b)))
    return pow(a, b, 1337)
print(superPow(2, [1, 0]))