def minimumRounds(tasks):
    from collections import Counter
    from math import ceil
    t = Counter(tasks)
    ans = 0
    for v in t.values():
        if v == 1:
            return -1
        ans += ceil(v / 3)
    return ans
print(minimumRounds([2,2,3,3,2,4,4,4,4,4]))
