import heapq
def findKthLargest(nums, k):
    ans = 0
    nums = [-i for i in nums]
    heapq.heapify(nums)
    n = 0
    while n < k:
        ans = heapq.heappop(nums)
        n += 1
    return -ans
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))