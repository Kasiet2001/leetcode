def minimumRightShifts(nums):
    s = sorted(nums)
    if s == nums:
        return 0
    ind = nums.index(min(nums))
    if nums[ind:] + nums[:ind] == s:
        return len(nums) - ind
    return -1
print(minimumRightShifts([1,3,5]))