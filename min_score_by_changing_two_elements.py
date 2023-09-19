def minimizeSum(nums):
    nums.sort()
    return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])
print(minimizeSum([1,4,3]))