def findValueOfPartition(nums):
    nums.sort()
    return min([nums[i] - nums[i - 1] for i in range(1, len(nums))])
print(findValueOfPartition([100,1,10]))