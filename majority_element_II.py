def majorityElement(nums):
    return [i for i in set(nums) if nums.count(i) > len(nums) / 3]
print(majorityElement([1]))