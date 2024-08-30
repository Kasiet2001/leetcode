import heapq
def getFinalState(nums, k, multiplier):
    n = len(nums)
    q = [(nums[i], i) for i in range(n)]
    heapq.heapify(q)
    while k > 0:
        v, idx = heapq.heappop(q)
        nums[idx] = v * multiplier
        heapq.heappush(q, (v * multiplier, idx))
        k -= 1
    return nums
print(getFinalState([2,1,3,5,6], 5, 2))
