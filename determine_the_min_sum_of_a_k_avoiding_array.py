def minimumSum(n, k):
    res = set()
    num = 1
    while len(res) < n:
        if k - num not in res:
            res.add(num)
        num += 1
    return sum(res)
print(minimumSum(5, 4))
