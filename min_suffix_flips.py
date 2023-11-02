def minFlips(target):
    ans = 0
    n = '0'
    for i in target:
        if n != i:
            ans += 1
            n = i
    return ans
print(minFlips("10111"))