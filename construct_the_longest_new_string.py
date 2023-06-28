def longestString(x, y, z):
    minimum = min(x, y)
    if x == y:
        return x * 4 + z * 2
    else:
        return minimum * 2 + (minimum + 1) * 2 + z * 2
print(longestString(3, 2, 2))