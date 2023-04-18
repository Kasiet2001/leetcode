def minimumAverageDifference(nums):
    if len(nums) < 2:
        return 0
    s = sum(nums)
    v = []
    ind = 1
    l = len(nums) - 1
    f = nums[0]
    while l > 0:
        v.append(abs(f // ind - (s - f) // l))
        f += nums[ind]
        ind += 1
        l -= 1
    v.append(abs(s // len(nums)))
    return v.index(min(v))
print(minimumAverageDifference([2,5,3,9,5,3]))
