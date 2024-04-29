def minOperationsToMakeMedianK(nums, k):
    nums.sort()
    mid = len(nums) // 2
    ans = 0
    if nums[mid] < k:
        for i in range(mid, len(nums)):
            if nums[i] < k:
                ans += k - nums[i]
    else:
        for i in range(mid + 1):
            if nums[i] > k:
                ans += nums[i] - k
    return ans
print(minOperationsToMakeMedianK([1,2,3,4,5,6], 4))