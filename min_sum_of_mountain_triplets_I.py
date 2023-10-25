def minimumSum(nums):
    pref_min = [nums[0]] * len(nums)
    suf_min = [nums[-1]] * len(nums)
    for i in range(1, len(nums)):
        pref_min[i] = min(pref_min[i - 1], nums[i])
    for i in range(len(nums) - 2, -1, -1):
        suf_min[i] = min(suf_min[i + 1], nums[i])
    ans = float('inf')
    for i in range(1, len(nums) - 1):
        if pref_min[i - 1] < nums[i] and suf_min[i + 1] < nums[i]:
            ans = min(ans, pref_min[i - 1] + nums[i] + suf_min[i + 1])
    return -1 if ans == float('inf') else ans
