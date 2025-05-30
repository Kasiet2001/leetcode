def closestMeetingNode(edges, node1, node2):
    prevMaxDist = float('inf')
    n = len(edges)

    def bfs(edges, node, n):
        d = [-1] * n
        dist = 0
        while d[node] == -1 and node != -1:
            d[node] = dist
            dist += 1
            node = edges[node]
        return d
    edges1 = bfs(edges, node1, n)
    edges2 = bfs(edges, node2, n)

    ans = -1

    for i in range(len(edges1)):
        if edges1[i] != -1 and edges2[i] != -1:
            maxDist = max(edges1[i], edges2[i])
            if prevMaxDist > maxDist:
                prevMaxDist = maxDist
                ans = i
    return ans
print(closestMeetingNode([2,2,3,-1], 0, 1))


