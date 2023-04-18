def findErrorNums(nums):
    return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]
print(findErrorNums([1,2,2,4]))