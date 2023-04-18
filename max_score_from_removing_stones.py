def maximumScore(a, b, c):
    a, b, c = sorted((a, b, c))
    if a + b < c:
        return a + b
    return (a + b + c) // 2
print(maximumScore(2, 4, 6))