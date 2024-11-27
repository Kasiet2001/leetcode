def findChampion(n, edges):
    e = {i: 1 for i in range(n)}
    for s, w in edges:
        if w in e:
            e.pop(w)
    ans = list(e.keys())
    return ans[0] if len(ans) == 1 else -1
print(findChampion(3, [[0,1],[1,2]]))