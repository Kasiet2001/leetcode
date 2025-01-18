def maxAdjacentDistance(nums):
    res = 0
    for i in range(1, len(nums)):
        res = max(res, abs(nums[i] - nums[i - 1]))
    return max(res, abs(nums[-1] - nums[0]))
print(maxAdjacentDistance([1,2,4]))