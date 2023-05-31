import heapq
import math
def minStoneSum(piles, k):
    heap = []
    for i in piles:
        heap.append(-i)
    heapq.heapify(heap)
    for _ in range(k):
        st = heapq.heappop(heap)
        heapq.heappush(heap, math.floor(st / 2))
    return -sum(heap)
print(minStoneSum([4,3,6,7], 3))