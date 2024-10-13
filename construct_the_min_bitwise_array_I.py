
def minBitwiseArray(nums):
    n = len(nums)
    ans = [-1] * n

    for i in range(n):
        for val in range(1, nums[i] + 1):
            if val | (val + 1) == nums[i]:
                ans[i] = val
                break
    return ans
print(minBitwiseArray([2,3,5,7]))