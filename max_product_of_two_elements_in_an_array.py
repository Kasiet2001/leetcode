def maxProduct(nums):
    ans = 0
    curr_max = 0
    for i in range(len(nums)):
        ans = max(ans, (curr_max - 1) * (nums[i] - 1))
        curr_max = max(curr_max, nums[i])
    return ans
print(maxProduct([1,5,4,5]))