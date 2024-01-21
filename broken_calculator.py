def brokenCalc(startValue, target):
    ans = 0
    while target > startValue:
        ans += 1
        if not target % 2:
            target //= 2
        else:
            target += 1
    return ans + startValue - target
print(brokenCalc(3, 11))