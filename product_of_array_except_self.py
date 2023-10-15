def productExceptSelf(nums):
    n = len(nums)
    prefix = 1
    postfix = 1
    ans = [0] * n
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]
    for j in range(n - 1, -1, -1):
        ans[j] *= postfix
        postfix *= nums[j]
    return ans
print(productExceptSelf([1,2,3,4]))