def findDisappearedNumbers(nums):
    return sorted(set([i for i in range(1, len(nums) + 1)]) - set(nums))
print(findDisappearedNumbers([1, 1]))