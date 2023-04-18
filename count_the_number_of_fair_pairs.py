def countFairPairs(nums, lower, upper):
    nums.sort()
    i = j = len(nums) - 1
    res = 0
    for ind, num in enumerate(nums):
        while i >= 0 and num + nums[i] >= lower:
            i -= 1
        while j >= 0 and num + nums[j] > upper:
            j -= 1
        res += j - i
        if i < ind <= j:
            res -= 1
    return res // 2
print(countFairPairs([0,1,7,4,4,5],3, 6))