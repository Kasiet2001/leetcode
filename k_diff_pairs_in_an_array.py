def findPairs(nums, k):
    from collections import Counter
    nums = Counter(nums)
    ans = 0
    for i in nums:
        if k > 0 and i + k in nums or k == 0 and nums[i] > 1:
            ans += 1
    return ans
print(findPairs([3,1,4,1,5], 2))