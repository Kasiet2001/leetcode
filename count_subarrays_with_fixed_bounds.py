def countSubarrays(nums, minK, maxK):
    ans = 0
    left = right = idx = -1
    for i, num in enumerate(nums):
        if not minK <= num <= maxK:
            idx = i
        if minK == num:
            left = i
        if maxK == num:
            right = i
        ans += max(0, min(left, right) - idx)
    return ans
print(countSubarrays([2,3,2,1,3,5,2,7,5], 1, 5))