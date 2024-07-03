def minDifference(nums):
    if len(nums) < 5:
        return 0
    nums.sort()
    ans = float('inf')
    lg = len(nums) - 4
    for sm in range(4):
        ans = min(ans, nums[lg] - nums[sm])
        lg += 1
    return ans
print(minDifference([5,3,2,4]))