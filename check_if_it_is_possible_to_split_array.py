def canSplitArray(nums, m):
    if len(nums) <= 2:
        return True
    for i in range(1, len(nums)):
        if nums[i - 1] + nums[i] >= m:
            return True
    return False
print(canSplitArray([2, 1, 3], 5))
