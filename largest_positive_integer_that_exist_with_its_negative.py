def findMaxK(nums):
    pos = dict()
    ans = -1
    for num in nums:
        if num * -1 in pos:
            ans = max(ans, abs(num))
        pos[num] = 1
    return ans
print(findMaxK([-1,2,-3,3]))