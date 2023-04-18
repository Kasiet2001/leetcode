def equalPairs(grid):
    from collections import Counter
    ans = 0
    t = Counter(tuple(i) for i in grid)
    for i in zip(*grid):
        if i in t:
            ans += t[i]
    return ans
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))