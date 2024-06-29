from collections import deque
def getAncestors(n, edges):
    adjacency_list = [[] for i in range(n)]
    for frm, to in edges:
        adjacency_list[to].append(frm)

    def find_ancestors(curr):
        q = deque(adjacency_list[curr])
        ancestors = []
        visited = set()
        while q:
            node = q.pop()
            if node not in visited:
                q.extend(adjacency_list[node])
                ancestors.append(node)
                visited.add(node)
        ancestors = sorted(ancestors)
        return ancestors

    ancestors_list = []
    for i in range(n):
        ancestors_list.append(find_ancestors(i))
    return ancestors_list
print(getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))