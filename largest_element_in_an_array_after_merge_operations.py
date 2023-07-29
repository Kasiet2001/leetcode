def maxArrayValue(nums):
    ans = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] <= ans:
            ans = ans + nums[i]
        else:
            ans = nums[i]
    return ans
print(maxArrayValue([5,3,3]))