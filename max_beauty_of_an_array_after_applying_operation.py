def maximumBeauty(nums, k):
    nums.sort()
    ans = 0
    left = 0
    for right in range(len(nums)):
        while nums[right] - nums[left] > 2 * k:
            left += 1
        ans = max(ans, right - left + 1)
    return ans
print(maximumBeauty([4,6,1,2], 2))