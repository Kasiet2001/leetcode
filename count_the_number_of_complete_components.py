from collections import defaultdict
def countCompleteComponents(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    complete = 0
    for vertex in range(n):
        if not visited[vertex]:
            queue = [vertex]
            visited[vertex] = True
            components = []
            while queue:
                node = queue.pop(0)
                components.append(node)
                for nei in graph[node]:
                    if not visited[nei]:
                        queue.append(nei)
                        visited[nei] = True
            is_complete = True
            for n in components:
                if len(graph[n]) != len(components) - 1:
                    is_complete = False
                    break
            if is_complete:
                complete += 1
    return complete
print(countCompleteComponents(4, [[1,0],[2,0],[3,1],[3,2]]))