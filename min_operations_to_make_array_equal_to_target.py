import heapq
def minimumOperations(nums, target):
    diff = [nums[i] - target[i] for i in range(len(nums))]
    ans = 0
    i = 0
    increasing = []
    decreasing = []
    n = 0
    while i < len(nums):
        while diff[i] > 0:
            increasing.append(diff[i])
            i += 1
        while increasing:
            m = heapq.heappop(increasing)
            n += m
            ans += 1
print(minimumOperations([9,2,6,10,4,8,3,4,2,3], [9,5,5,1,7,9,8,7,6,5]))
