def restoreArray(adjacentPairs):
    from collections import defaultdict
    adj, ans, n = defaultdict(list), [], len(adjacentPairs) + 1
    for a, b in adjacentPairs:
        adj[a] += [b]
        adj[b] += [a]
    prev = -math.inf
    for k, v in adj.items():
        if len(v) == 1:
            ans += [k]
            break
    while len(ans) < n:
        for next in adj.pop(ans[-1]):
            if next != prev:
                prev = ans[-1]
                ans += [next]
                break
    return ans
print(restoreArray([[4,-10],[-1,3],[4,-3],[-3,3]]))