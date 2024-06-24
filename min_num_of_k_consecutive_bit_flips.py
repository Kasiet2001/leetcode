def minKBitFlips(nums, k):
    curr_window_flips = 0
    res = 0
    for i in range(len(nums)):
        if i - k >= 0 and nums[i - k] == 2:
            curr_window_flips -= 1
        if (nums[i] + curr_window_flips) % 2 == 0:
            if i + k > len(nums):
                return -1
            res += 1
            curr_window_flips += 1
            nums[i] = 2
    return res
print(minKBitFlips([0,0,0,1,0,1,1,0], 3))