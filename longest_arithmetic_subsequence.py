from collections import defaultdict
def longestArithSeqLength(nums):
    dp = defaultdict(dict)
    n = len(nums)
    ans = 1
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff not in dp[j]:
                dp[j][diff] = 1
            if diff not in dp[i]:
                dp[i][diff] = 0
            dp[i][diff] = dp[j][diff] + 1
            ans = max(ans, dp[i][diff])
    return ans
print(longestArithSeqLength([9,4,7,2,10]))