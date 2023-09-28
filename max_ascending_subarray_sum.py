def maxAscendingSum(nums):
    ans = 0
    res = nums[0]
    curr = nums[0]
    for i in range(1, len(nums)):
        if curr >= nums[i]:
            ans = max(res, ans)
            res = nums[i]
        else:
            res += nums[i]
        curr = nums[i]
    return max(ans, res)
print(maxAscendingSum([12,17,15,13,10,11,12]))