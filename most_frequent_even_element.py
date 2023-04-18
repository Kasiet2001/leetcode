def mostFrequentEven(nums):
    d = {}
    f = []
    for i in nums:
        if i % 2 == 0:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    if len(d) == 0:
        return -1
    else:
        m = max(d.values())
        for k, v in d.items():
            if v == m:
                f.append(k)
        return min(f)
print(mostFrequentEven( [29,47,21,41,13,37,25,7]))