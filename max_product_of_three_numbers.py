def maximumProduct(nums):
    nums = sorted(nums)
    if len(nums) == 3:
        return nums[0] * nums[1] * nums[2]
    elif (nums[0] * nums[1]) > (nums[-2] * nums[-3]) and nums[-1] >= 0:
        return nums[0] * nums[1] * nums[-1]
    return nums[-1] * nums[-2] * nums[-3]
print(maximumProduct([-8, -7, -1, 10, 20]))