from collections import deque
def shortestDistanceAfterQueries(n, queries):
    adj = [[i + 1] for i in range(n)]

    def bfs():
        q = deque()
        q.append((0, 0))
        visit = set()
        visit.add((0, 0))
        while q:
            cur, length = q.popleft()
            if cur == n - 1:
                return length
            for nei in adj[cur]:
                if nei not in visit:
                    q.append((nei, length + 1))
                    visit.add(nei)

    res = []
    for scr, dst in queries:
        adj[scr].append(dst)
        res.append(bfs())
    return res
print(shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))