def isMonotonic(nums):
    if len(nums) <= 2:
        return True
    decr = 0
    incr = 0
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            incr += 1
        elif nums[i - 1] > nums[i]:
            decr += 1
        if incr and decr:
            return False
    return True
print(isMonotonic([2,2,2]))
