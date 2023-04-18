def findClosestNumber(nums):
    ind = [abs(i) for i in nums].index(min([abs(i) for i in nums]))
    return nums[ind] if abs(nums[ind]) not in nums else abs(nums[ind])
print(findClosestNumber([2,-1,1]))