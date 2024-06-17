def judgeSquareSum(c):
    start = 0
    end = int(c ** 0.5) + 1
    while start < end:
        if start ** 2 + end ** 2 > c:
            end -= 1
        elif start ** 2 + end ** 2 < c:
            start += 1
        else:
            return True
    return start ** 2 + end ** 2 == c
print(judgeSquareSum(5))