def countWays(nums):
    nums.sort()
    ans = 0
    n = len(nums)
    if nums[0] > 0:
        ans += 1
    for i in range(1, len(nums)):
        if nums[i - 1] < i and i < nums[i]:
            ans += 1
    if nums[-1] < len(nums):
        ans += 1
    return ans
print(countWays([6,0,3,3,6,7,2,7]))
