from collections import Counter
def findLHS(nums):
    ans = 0
    n = Counter(nums)
    for i in nums:
        if i - 1 in n:
            ans = max(ans, n[i] + n[i - 1])
    return ans
print(findLHS([1,1,1,1]))