def maximumBeauty(items, queries):
    items.sort()
    ans = [0] * len(queries)
    p = ind = 0
    q = ((x, i) for i, x in enumerate(queries))
    for x, i in sorted(q):
        while ind < len(items) and items[ind][0] <= x:
            p = max(p, items[ind][1])
            ind += 1
        ans[i] = p
    return ans
print(maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]))