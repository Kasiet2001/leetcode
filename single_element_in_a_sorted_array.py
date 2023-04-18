def singleNonDuplicate(nums):
    n = [i * 2 for i in set(nums)]
    return sum(n) - sum(nums)
print(singleNonDuplicate([3,3,7,7,10,11,11]))