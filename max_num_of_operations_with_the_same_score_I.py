def maxOperations(nums):
    score = nums[0] + nums[1]
    ans = 1
    for i in range(3, len(nums), 2):
        if nums[i] + nums[i - 1] != score:
            return ans
        ans += 1
    return ans
print(maxOperations([3,2,1,4,5, 0]))