def isSameAfterReversals(num):
    return int(str(int(str(num)[::-1]))[::-1]) == num
    # return num == 0 or not num % 10 == 0
print(isSameAfterReversals(526))