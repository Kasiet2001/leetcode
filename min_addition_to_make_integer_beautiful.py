def makeIntegerBeautiful(n, target):
    ans = 0
    added = 0
    m = 10
    if n <= target:
        return ans
    while sum([int(i) for i in str(n)]) > target:
        added = m - n % m
        if added != m:
            n += added
            ans += added
        m *= 10
    return ans
print(makeIntegerBeautiful(467, 6))