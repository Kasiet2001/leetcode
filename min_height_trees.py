from collections import deque, defaultdict
def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    edg_cnt = {}
    leaves = deque()
    for k, v in adj.items():
        if len(v) == 1:
            leaves.append(k)
        edg_cnt[k] = len(v)

    while leaves:
        if n <= 2:
            return list(leaves)
        for i in range(len(leaves)):
            node = leaves.popleft()
            n -= 1
            for j in adj[node]:
                edg_cnt[j] -= 1
                if edg_cnt[j] == 1:
                    leaves.append(j)

print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
