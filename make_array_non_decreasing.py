def maximumPossibleSize(nums):
    value = 0
    ans = 0
    for num in nums:
        if num >= value:
            value = num
            ans += 1
    return ans
print(maximumPossibleSize([1,2,3]))