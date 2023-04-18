def findDuplicate(nums):
    return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))
print(findDuplicate([2,2,2,2,2,2]))