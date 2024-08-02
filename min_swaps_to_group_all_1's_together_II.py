def minSwaps(nums):
    n = len(nums)
    total_ones = sum(nums)
    l = 0
    window_ones = max_window_ones = 0
    for r in range(n * 2):
        if nums[r % n]:
            window_ones += 1
        if r - l + 1 > total_ones:
            window_ones -= nums[l % n]
            l += 1
        max_window_ones = max(max_window_ones, window_ones)
    return total_ones - max_window_ones
print(minSwaps([0,1,1,1,0,0,1,1,0]))