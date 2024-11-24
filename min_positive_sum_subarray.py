def minimumSumSubarray(nums, l, r):
    ans = float('inf')
    n = 0
    for i in range(len(nums) - l + 1):
        while l + n <= r:
            m = sum(nums[i: i + l + n])
            if m > 0:
                ans = min(ans, m)
            n += 1
        n = 0
    return ans if ans != float('inf') else -1
print(minimumSumSubarray([-2,2,-3,1], 2, 3))