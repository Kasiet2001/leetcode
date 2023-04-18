def majorityElement(nums):
    return [i for i in set(nums) if nums.count(i) > len(nums) / 2][0]
print(majorityElement([3,2,3]))