def canSortArray(nums):
    i = last = 0
    while i < len(nums):
        n = nums[i].bit_count()
        j = i + 1
        maximum = minimum = nums[i]
        while j < len(nums) and n == nums[j].bit_count():
            maximum = max(maximum, nums[j])
            minimum = min(minimum, nums[j])
            j += 1
        if last > minimum:
            return False
        last = maximum
        i = j
    return True
print(canSortArray([3,16,8,4,2]))
