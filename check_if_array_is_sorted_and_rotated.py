def check(nums):
    n = len(nums)
    if n <= 1:
        return True
    r = 0
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            r += 1
    if nums[0] < nums[n - 1]:
        r += 1
    return r <= 1
print(check([8,5,4,5,1,4,5,2,2]))