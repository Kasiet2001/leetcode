import heapq
def resultsArray(queries, k):
    max_heap = []
    results = []

    for x, y in queries:
        distance = abs(x) + abs(y)

        if len(max_heap) < k:
            heapq.heappush(max_heap, -distance)
        else:
            if distance < -max_heap[0]:
                heapq.heapreplace(max_heap, -distance)

        if len(max_heap) < k:
            results.append(-1)
        else:
            results.append(-max_heap[0])

    return results
print(resultsArray([[1,2],[3,4],[2,3],[-3,0]], 2))