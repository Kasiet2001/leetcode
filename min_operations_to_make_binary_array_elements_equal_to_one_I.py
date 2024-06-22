def minOperations(nums):
    n = len(nums)
    operations = 0
    if n < 3:
        return 0 if all(x == 1 for x in nums) else -1

    i = 0
    while i <= n - 3:
        if nums[i] == 0:
            nums[i] = 1 - nums[i]
            nums[i + 1] = 1 - nums[i + 1]
            nums[i + 2] = 1 - nums[i + 2]
            operations += 1
        i += 1
    if all(x == 1 for x in nums):
        return operations
    else:
        return -1