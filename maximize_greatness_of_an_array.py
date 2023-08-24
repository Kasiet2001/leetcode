def maximizeGreatness(nums):
    nums.sort()
    res = 0
    for i in nums:
        if nums[res] < i:
            res += 1
    return res
print(maximizeGreatness([1,3,5,2,1,3,1]))