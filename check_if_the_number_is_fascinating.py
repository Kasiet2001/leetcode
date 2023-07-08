def isFascinating(n):
    m = str(n) + str(n * 2) + str(n * 3)
    return sorted(m) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(isFascinating(100))