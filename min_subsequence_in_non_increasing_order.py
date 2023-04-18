def minSubsequence(nums):
    sub = []
    nums = sorted(nums, reverse=True)
    for i in range(len(nums)):
        sub.append(nums[i])
        if sum(sub) > sum(nums[i + 1:]):
            return sub
print(minSubsequence([4,4,7,6,7]))