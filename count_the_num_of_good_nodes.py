from collections import defaultdict
def countGoodNodes(edges):
    n = len(edges) + 1
    tree = defaultdict(list)

    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)


    subtree_size = [0] * n
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        size = 1
        for neighbor in tree[node]:
            if not visited[neighbor]:
                size += dfs(neighbor)
        subtree_size[node] = size
        return size

    dfs(0)

    good_nodes = 0

    for node in range(n):
        child_sizes = set()
        for child in tree[node]:
            if subtree_size[child] < subtree_size[node]:
                child_sizes.add(subtree_size[child])

        if len(child_sizes) <= 1:
            good_nodes += 1

    return good_nodes
print(countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
