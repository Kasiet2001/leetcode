from collections import deque, defaultdict
def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])
    visited = set([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False
print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
