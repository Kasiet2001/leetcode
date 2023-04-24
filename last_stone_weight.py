def lastStoneWeight(stones):
    import heapq
    stones = [-i for i in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if y != x:
            heapq.heappush(stones, y - x)
    return -stones[0] if len(stones) > 0 else 0
print(lastStoneWeight([2, 2]))