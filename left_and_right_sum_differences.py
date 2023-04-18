def leftRigthDifference(nums):
    l = sum(nums)
    r = 0
    ans = []
    for i in nums:
        r += i
        ans.append(abs(l - r))
        l -= i
    return ans
print(leftRigthDifference([10,4,8,3]))
