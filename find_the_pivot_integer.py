def pivotInteger(n):
    pivot = (n**2 + n) / 2
    if pivot % pivot ** 0.5 == 0:
        return int(pivot ** 0.5)
    return -1
print(pivotInteger(1))
