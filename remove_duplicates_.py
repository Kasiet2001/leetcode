def removeDuplicates(nums):
    ind = 0
    for i in range(min(nums), max(nums) + 1):
        if i in nums:
            nums[ind] = i
            ind += 1
    return ind
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))