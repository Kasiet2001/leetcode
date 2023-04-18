def sumOfThree(num):
    if num % 3 == 0:
        num //= 3
        return [num - 1, num, num + 1]
    return []
print(sumOfThree(33))