def longestAlternatingSubarray(nums, threshold):
    res = []
    ans = 0
    for i in nums:
        if i > threshold:
            res = []
        elif not res and i % 2 == 0:
                res.append(i)
        elif len(res) > 0:
            if res[-1] % 2 != i % 2:
                res.append(i)
            elif i % 2 == 0:
                res = [i]
            else:
                res = []
        ans = max(ans, len(res))
    return ans
print(longestAlternatingSubarray([2,3,3,10], 18))