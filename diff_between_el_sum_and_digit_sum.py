def differenceOfSum(nums):
    n = sum(nums)
    s = [str(i) for i in nums]
    d = sum([int(i) for i in ''.join(s)])
    return abs(n - d)
print(differenceOfSum([1,2,3,4]))