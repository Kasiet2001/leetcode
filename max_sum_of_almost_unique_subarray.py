from collections import Counter
def maxSum(nums, m, k):
    ans = 0
    for i in range(len(nums) - k + 1):
        if len(set(nums[i:k + i])) >= m:
            ans = max(ans, sum(nums[i:k + i]))
    return ans
print(maxSum([1], 1, 1))