from collections import defaultdict
import heapq
def minimumCost(source, target, original, changed, cost):
    adj = defaultdict(list)
    for scr, dst, cur_cost in zip(original, changed, cost):
        adj[scr].append((dst, cur_cost))

    def dijkstra(scr):
        heap = [(0, scr)]
        min_cost_map = {}
        while heap:
            cost, node = heapq.heappop(heap)
            if node in min_cost_map:
                continue
            min_cost_map[node] = cost
            for nei, nei_cost in adj[node]:
                heapq.heappush(heap, (cost + nei_cost, nei))
        return min_cost_map

    min_cost_maps = {c: dijkstra(c) for c in set(source)}
    res = 0
    for scr, dst in zip(source, target):
        if dst not in min_cost_maps[scr]:
            return -1
        res += min_cost_maps[scr][dst]
    return res
print(minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))