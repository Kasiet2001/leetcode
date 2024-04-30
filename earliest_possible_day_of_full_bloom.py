def earliestFullBloom(plantTime, growTime):
    n = list(zip(plantTime, growTime))
    data = sorted(n, key=lambda x: -x[1])
    res = 0
    m = 0
    for plant, grow in data:
        m += plant
        res = max(res, m + grow)
    return res
print(earliestFullBloom([1,4,3], [2,3,1]))
