def findPrefixScore(nums):
    ans = []
    maximum = 0
    n = 0
    for i in nums:
        maximum = max(maximum, i)
        n += i + maximum
        ans.append(n)
    return ans
print(findPrefixScore([1,1,2,4,8,16]))