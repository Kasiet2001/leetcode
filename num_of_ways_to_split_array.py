def waysToSplitArray(nums):
    ans = 0
    total = sum(nums)
    prefix = nums[0]
    for i in range(1, len(nums)):
        if prefix >= total - prefix:
            ans += 1
        prefix += nums[i]
    return ans
print(waysToSplitArray([2,3,1,0]))