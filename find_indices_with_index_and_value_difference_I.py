def findIndices(nums, indexDifference, valueDifference):
    if indexDifference == 0 and valueDifference == 0:
        return [0, 0]
    for i in range(len(nums) - 1):
        for j in range(i + indexDifference, len(nums)):
            if abs(nums[i] - nums[j]) >= valueDifference:
                return [i, j]
    return [-1, -1]