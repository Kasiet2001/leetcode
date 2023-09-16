def numberOfArithmeticSlices(nums):
    ans = 0
    curr = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            curr += 1
            ans += curr
        else:
            curr = 0
    return ans
print(numberOfArithmeticSlices([1,2,3,4]))