def createTargetArray(nums, index):
    n = []
    for i in range(len(nums)):
        n.insert(index[i], nums[i])
    return n
print(createTargetArray([1,2,3,4,0], [0,1,2,3,0]))