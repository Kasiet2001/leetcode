def minimumReplacement(nums):
    n = len(nums)
    last = nums[n - 1]
    ans = 0
    for i in range(n - 2, -1, -1):
        if nums[i] > last:
            m = nums[i] // last
            if nums[i] % last:
                m += 1
            last = nums[i] // m
            ans += m - 1
        else:
            last = nums[i]
    return ans
print(minimumReplacement([3,11,3]))
