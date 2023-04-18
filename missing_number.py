def missingNumber(nums):
    m = [i for i in range(len(nums) + 1)]
    return [i for i in set(m) - set(nums)][0]
print(missingNumber([0,1]))