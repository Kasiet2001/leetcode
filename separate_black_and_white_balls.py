def minimumSteps(s):
    swaps = 0
    ans = 0
    for i in s:
        if i == '1':
            swaps += 1
        else:
            ans += swaps
    return ans
print(minimumSteps("111111111100100010"))