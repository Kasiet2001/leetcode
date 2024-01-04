def largestPerimeter(nums):
    nums.sort()
    ans = sum(nums)
    sides = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] >= ans - nums[i]:
            ans -= nums[i]
            sides -= 1
            if sides < 3:
                return -1
    return ans
print(largestPerimeter([5,5,50]))