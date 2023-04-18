def singleNumber(nums):
    return [i for i in set(nums) if nums.count(i) == 1]
print(singleNumber([-1,0]))