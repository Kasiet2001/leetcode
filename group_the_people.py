def groupThePeople(groupSizes):
    groups = {}
    ans = []
    for i, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = []
        groups[size].append(i)
        if len(groups[size]) == size:
            ans.append(groups[size])
            groups[size] = []
    return ans
print(groupThePeople([3,3,3,3,3,1,3]))