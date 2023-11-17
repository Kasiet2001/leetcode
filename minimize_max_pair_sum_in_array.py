def minPairSum(nums):
    ans = 0
    nums.sort()
    right = len(nums) - 1
    left = 0
    while left < right:
        ans = max(ans, nums[left] + nums[right])
        left += 1
        right -= 1
    return ans
print(minPairSum([4,1,5,1,2,5,1,5,5,4]))