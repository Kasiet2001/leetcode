def hasIncreasingSubarrays(nums, k):
    n = len(nums)

    for i in range(n - 2 * k + 1):
        is_first_increasing = all(nums[j] < nums[j + 1] for j in range(i, i + k - 1))

        is_second_increasing = all(nums[j] < nums[j + 1] for j in range(i + k, i + 2 * k - 1))

        if is_first_increasing and is_second_increasing:
            return True

    return False
print(hasIncreasingSubarrays([8,-4,-1,16,20], 2))
