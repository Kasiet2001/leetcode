from collections import defaultdict, deque
import heapq
def maxProbability(n, edges, succProb, start_node, end_node):
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, succProb[i]))
        adj[v].append((u, succProb[i]))

    max_prob = [0.0] * n
    max_prob[start_node] = 1.0

    pq = [(-1.0, start_node)]
    while pq:
        curr_prob, curr_node = heapq.heappop(pq)
        if curr_node == end_node:
            return -curr_prob
        for nxt_node, path_prob in adj[curr_node]:
            if -curr_prob * path_prob > max_prob[nxt_node]:
                max_prob[nxt_node] = -curr_prob * path_prob
                heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
    return 0.0
print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))