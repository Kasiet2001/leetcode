def countPairs(nums, k):
    t = 0
    if len(nums) == len(set(nums)):
        return t
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and (i * j) % k == 0:
                t += 1
    return t
print(countPairs([1,2,3,4], 1))