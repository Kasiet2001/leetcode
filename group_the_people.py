def groupThePeople(groupSizes):
    from collections import defaultdict
    c = defaultdict(list)
    for k, v in enumerate(groupSizes):
        c[v].append(k)
    return [l[i:i + s] for s, l in c.items() for i in range(0, len(l), s)]
print(groupThePeople([3,3,3,3,3,1,3]))