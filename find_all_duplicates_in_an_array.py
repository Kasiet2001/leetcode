def findDuplicates(nums):
    dup = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            dup.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return dup
print(findDuplicates([4,3,2,7,8,2,3,1]))