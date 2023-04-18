def triangularSum(nums):
    l = len(nums)
    while l > 1:
        for i in range(l - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        l -= 1
    return nums[0]
print(triangularSum([1,2,3,4,5]))