def rob(nums):
    count = len(nums)
    if count == 0:
        return 0
    elif count == 1:
        return nums[0]
    elif count == 2:
        return max(nums)
    m = nums[:]
    m[1] = max(nums[0], nums[1])
    for i in range(2, count):
        m[i] = max(m[i - 1], nums[i] + m[i - 2])
    return m[count - 1]
print(rob([1,3,1,3,100]))