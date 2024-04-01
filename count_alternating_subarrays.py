def countAlternatingSubarrays(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            dp[i] = dp[i - 1] + 1
    return sum(dp)
print(countAlternatingSubarrays([1,0,1,0]))