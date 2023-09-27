import heapq
from collections import Counter
def minLengthAfterRemovals(nums):
    count = [-i for i in Counter(nums).values()]
    heapq.heapify(count)
    while len(count) > 1:
        a = -heapq.heappop(count)
        b = -heapq.heappop(count)
        if a > 1:
            heapq.heappush(count, -a + 1)
        if b > 1:
            heapq.heappush(count, -b + 1)
    return -sum(count)
print(minLengthAfterRemovals([1,1,2,2,3,3]))