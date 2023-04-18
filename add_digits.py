def addDigits(num):
    while num > 9:
        num = sum([int(i) for i in str(num)])
    return num
print(addDigits(38))