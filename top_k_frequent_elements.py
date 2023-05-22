from collections import Counter
import heapq
def topKFrequent(nums, k):
    ans = []
    d = Counter(nums)
    n = [(-v, k) for k, v in d.items()]
    heapq.heapify(n)
    for i in range(k):
        elem = heapq.heappop(n)
        ans.append(elem[1])
    return ans
print(topKFrequent([1,1,1,2,2,3], 2))