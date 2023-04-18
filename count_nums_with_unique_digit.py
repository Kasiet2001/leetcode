def countNumbersWithUniqueDigits(n):
    ans = 1
    t = 1
    for i in range(1, n + 1):
        ans += t * 9
        t = t * (10 - i)
    return ans
print(countNumbersWithUniqueDigits(2))