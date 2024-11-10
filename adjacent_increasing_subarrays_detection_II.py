def maxIncreasingSubarrays(nums):
    n = len(nums)
    if n < 2:
        return 0
    lengths = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            lengths[i] = lengths[i + 1] + 1

    def can_find_adjacent_increasing(k):
        for i in range(n - 2 * k + 1):
            if lengths[i] >= k and lengths[i + k] >= k:
                return True
        return False

    left, right = 1, n // 2
    max_k = 0
    while left <= right:
        mid = (left + right) // 2
        if can_find_adjacent_increasing(mid):
            max_k = mid
            left = mid + 1
        else:
            right = mid - 1

    return max_k
print(maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))