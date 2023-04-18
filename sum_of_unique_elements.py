def sumOfUnique(nums):
    return sum([i for i in set(nums) if nums.count(i) == 1])
print(sumOfUnique([1,2,3,4,5]))