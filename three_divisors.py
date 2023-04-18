def isThree(n):
    amount = 0
    for i in range(1, n + 1):
        if n % i == 0:
            amount += 1
    return amount == 3
print(isThree(4))