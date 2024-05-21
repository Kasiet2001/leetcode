import bisect
def minAbsoluteDifference(nums, x):
    vals = []
    ans = float('inf')
    for i, v in enumerate(nums):
        if i >= x:
            bisect.insort(vals, nums[i - x])
            vals.sort()
            idx = bisect.bisect_left(vals, v)
            if idx:
                ans = min(ans, v - vals[idx - 1])
            if idx < len(vals):
                ans = min(ans, vals[idx] - v)
    return ans
print(minAbsoluteDifference([4,3,2,4], 2))