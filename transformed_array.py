def constructTransformedArray(nums):
    l = len(nums)
    ans = [0] * l
    for i in range(l):
        if nums[i] != 0:
            ans[i] = nums[(i + nums[i]) % l]
    return ans
print(constructTransformedArray([3,-2,1,1]))
