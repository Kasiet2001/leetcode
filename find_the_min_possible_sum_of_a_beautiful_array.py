def minimumPossibleSum(n, target):
    s = set()
    num = 1
    ans = 0
    while len(s) < n:
        if target - num not in s:
            s.add(num)
            ans += num
        num += 1
    return ans
print(minimumPossibleSum(2, 3))