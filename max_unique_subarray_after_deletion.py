def maxSum(nums):
    if max(nums) <= 0:
        return max(nums)
    seen = set()
    ans = 0
    for num in nums:
        if num not in seen and num > 0:
            ans += num
            seen.add(num)
    return ans
print(maxSum([1,1,0,1,1]))