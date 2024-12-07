def minOperations(nums, k):
    nums.sort(reverse=True)
    operations = 0

    while nums[0] != k:
        max_val = nums[0]
        if max_val <= k:
            break

        next_val = k
        for num in nums:
            if num < max_val:
                next_val = num
                break
        nums = [min(num, next_val) for num in nums]
        operations += 1

    return operations if all(num == k for num in nums) else -1
print(minOperations([9,7,5,3], 1))