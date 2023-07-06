def distinctDifferenceArray(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(len(set(nums[:i + 1])) - len(set(nums[i + 1:])))
    return ans
print(distinctDifferenceArray([1,2,3,4,5]))