def getMinDistance(nums, target, start):
    ans = float('inf')
    for i, n in enumerate(nums):
        if n == target:
            ans = min(ans, abs(i - start))
    return ans
print(getMinDistance([1,2,3,4,5], 5, 3))