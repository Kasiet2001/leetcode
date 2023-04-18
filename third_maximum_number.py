def thirdMax(nums):
    return set(nums)[-3] if len(nums) > 2 and len(set(nums)) > 2 else max(nums)
print(thirdMax([1, 1, 2]))
