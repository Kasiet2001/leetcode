def applyOperations(nums):
    n = len(nums)
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
    l = 0
    for r in range(1, n):
        if nums[l] == 0 and nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        if nums[l]:
            l += 1
    return nums
print(applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))