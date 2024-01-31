def minimumCost(nums):
    n = len(nums)
    s = nums[0]
    nums[1:n] = sorted(nums[1:n])
    s = s + nums[1] + nums[2]
    return s