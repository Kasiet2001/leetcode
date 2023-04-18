def maxSubsequence(nums, k):
    while len(nums) != k:
        nums.remove(min(nums))
    return nums
print(maxSubsequence([3,4,3,3],2))