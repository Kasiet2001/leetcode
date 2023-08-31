def countPairs(nums, target):
    nums.sort()
    ans = 0
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] >= target:
            right -= 1
        else:
            ans += right - left
            left += 1
    return ans
print(countPairs([-1,1,2,3,1], 2))