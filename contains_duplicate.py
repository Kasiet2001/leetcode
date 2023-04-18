def containsDuplicate(nums):
    return False if len(set(nums)) == len(nums) else True
print(containsDuplicate([1,2,3,4]))