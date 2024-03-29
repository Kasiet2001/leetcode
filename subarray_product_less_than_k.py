def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    total = 0
    product = 1
    left = 0
    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left += 1
        total += right - left + 1
    return total