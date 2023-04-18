def canBeIncreasing(nums):
    if len(set(nums)) < len(nums) - 1:
        return False
    for i in range(len(nums)):
        n = nums[:i] + nums[i + 1:]
        if n == sorted(n) and len(set(n)) == len(n):
            return True
    return False
print(canBeIncreasing([1,2,10,5,5,7]))