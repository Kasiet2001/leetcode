def minIncrementOperations(nums, k):
    dp = [0] * len(nums)
    dp[0], dp[1], dp[2] = max(0, k - nums[0]), max(0, k - nums[1]), max(0, k - nums[2])
    for i in range(3, len(nums)):
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3]) + max(0, k - nums[i])
    return min(dp[-1], dp[2], dp[-3])
print(minIncrementOperations([2,3,0,0,2], 4))