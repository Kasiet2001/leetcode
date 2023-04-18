def maxSatisfaction(satisfaction):
    ans = 0
    total = 0
    satisfaction.sort()
    while satisfaction and satisfaction[-1] + total > 0:
        total += satisfaction.pop()
        ans += total
    return ans
print(maxSatisfaction([-1,-8,0,5,-9]))