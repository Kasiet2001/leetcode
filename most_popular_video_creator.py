def mostPopularCreator(creators, ids, views):
    from collections import defaultdict
    v = defaultdict(int)
    id = {}
    n = 0
    for i in range(len(ids)):
        v[creators[i]] += views[i]
        if creators[i] in id:
            if id[creators[i]][0] < views[i]:
                id[creators[i]] = [views[i], ids[i]]
            elif id[creators[i]][0] == views[i] and ids[i] < id[creators[i]][1]:
                id[creators[i]] = [views[i], ids[i]]
        else:
            id[creators[i]] = [views[i], ids[i]]
        n = max(n, v[creators[i]])
    ans = []
    for creator in v:
        if v[creator] == n:
            ans.append([creator, id[creator][1]])
    return ans
print(mostPopularCreator(["alice","alice","alice"], ["a","b","c"], [1,2,2]))
