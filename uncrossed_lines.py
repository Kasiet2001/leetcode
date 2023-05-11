def maxUncrossedLines(nums1, nums2):
    prev = [0] * (len(nums2) + 1)
    for i in range(len(nums1)):
        dp = [0] * (len(nums2) + 1)
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[j + 1] = 1 + prev[j]
            else:
                dp[j + 1] = max(dp[j], prev[j + 1])
        prev = dp
    return prev[len(nums2)]
print(maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]))