from collections import defaultdict, deque
def assignEdgeWeights(edges):
    MOD = 10 ** 9 + 7
    tree = defaultdict(list)
    n = 0
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
        if u > n:
            n = u
        if v > n:
            n = v
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    max_depth = 0

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                max_depth = max(max_depth, depth[neighbor])
                queue.append(neighbor)

    if max_depth == 0:
        return 0

    return pow(2, max_depth - 1, MOD)
print(assignEdgeWeights([[1,2]]))