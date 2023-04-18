def findLengthOfLCIS(nums):
    if nums == []:
        return 0
    m = t = 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            t += 1
            m = max(m, t)
        else:
            t = 1
    return m
print(findLengthOfLCIS([2,2,2,2,2]))