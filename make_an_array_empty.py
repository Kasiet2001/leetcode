def countOperationsToEmptyArray(nums):
    p = {a: i for i, a in enumerate(nums)}
    ans = n = len(nums)
    nums.sort()
    for i in range(1, n):
        if p[nums[i]] < p[nums[i - 1]]:
            ans += n - i
    return ans
print(countOperationsToEmptyArray([1,2,4,3]))