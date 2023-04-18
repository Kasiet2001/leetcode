def maxKelements(nums, k):
    from math import ceil
    import heapq
    nums = [-i for i in nums]
    heapq.heapify(nums)
    res = 0
    for i in range(k):
        t = -heapq.heappop(nums)
        res += t
        heapq.heappush(nums, -ceil(t / 3))
    return res
print(maxKelements([672579538,806947365,854095676,815137524], 3))