def minCost(basket1, basket2):
    from collections import Counter
    b1 = Counter(basket1)
    last = []
    for f in basket2:
        b1[f] -= 1
    for k, v in b1.items():
        if v % 2 != 0:
            return -1
        last += [k] * abs(v // 2)
    minimum = min(basket1 + basket2)
    last.sort()
    return sum(min(minimum * 2, i) for i in last[0:len(last) // 2])
print(minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]))