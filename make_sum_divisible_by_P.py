def minSubarray(nums, p):
    total = sum(nums)
    remain = total % p
    if remain == 0:
        return 0
    res = len(nums)
    curr_sum = 0
    remain_to_idx = {0: -1}
    for i, n in enumerate(nums):
        curr_sum = (curr_sum + n) % p
        pref = (curr_sum - remain + p) % p
        if pref in remain_to_idx:
            length = i - remain_to_idx[pref]
            res = min(length, res)
        remain_to_idx[curr_sum] = i
    return -1 if res == len(nums) else res
print(minSubarray([6,3,5,2], 9))
