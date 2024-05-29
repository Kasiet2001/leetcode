def numSteps(s):
    num = int(s, 2)
    ans = 0
    while num != 1:
        if num % 2:
            num += 1
        else:
            num //= 2
        ans += 1
    return ans
print(numSteps("10"))