def sumOfGoodNumbers(nums, k):
    total_sum = 0
    n = len(nums)

    for i in range(n):
        left = nums[i - k] if i - k >= 0 else float('-inf')
        right = nums[i + k] if i + k < n else float('-inf')

        if nums[i] > left and nums[i] > right:
            total_sum += nums[i]

    return total_sum
print(sumOfGoodNumbers([2,1], 1))