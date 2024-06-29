from collections import deque
def getAncestors(n, edges):
    adjacency_list = [[] for i in range(n)]
    for frm, to in edges:
        adjacency_list[to].append(frm)
    ancestors_list = []
    for i in range(n):
        q = deque(adjacency_list[i])
        ancestors = []
        visited = set()
        while q:
            node = q.pop()
            if node not in visited:
                q.extend(adjacency_list[node])
                ancestors.append(node)
                visited.add(node)
        ancestors_list.append(sorted(ancestors))
    return ancestors_list
print(getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))