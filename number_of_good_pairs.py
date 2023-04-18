def numIdenticalPairs(nums):
    n = 0
    for i in range(len(sorted(nums))):
        if nums.count(nums[i]) > 1:
            n += nums[i + 1:].count(nums[i])
    return n
print(numIdenticalPairs([1,2,3,1,1,3]))