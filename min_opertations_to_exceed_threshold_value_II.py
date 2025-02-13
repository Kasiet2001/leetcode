import heapq
def minOperations(nums, k):
    heapq.heapify(nums)
    res = 0
    while nums[0] < k:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        heapq.heappush(nums, x * 2 + y)
        res += 1
    return res
print(minOperations([1,1,2,4,9], 20))