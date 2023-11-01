def threeSum(nums):
    nums.sort()
    ans = set()
    right = len(nums) - 1
    for i in range(len(nums)):
        left = i + 1
        while left < right:
            if sum([nums[i] + nums[left] + nums[right]]) == 0:
                ans.add((nums[i], nums[left], nums[right]))
                right -= 1
                left += 1
            elif sum([nums[i] + nums[left] + nums[right]]) > 0:
                right -= 1
            else:
                left += 1
        right = len(nums) - 1
    return ans
print(threeSum([0, 0, 0, 0]))


