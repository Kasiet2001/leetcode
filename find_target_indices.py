def targetIndices(nums, target):
    indices = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)
    return indices
print(targetIndices([1,2,5,2,3], 2))