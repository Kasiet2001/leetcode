from collections import Counter
def findShortestSubArray(nums):
    ans = len(nums)
    n = Counter(nums)
    maximum = max(n.values())
    ch = {k: v for k, v in n.items() if v >= maximum}
    for i in range(len(nums)):
        if nums[i] in ch:
            ch[nums[i]] -= 1
            if ch[nums[i]] == 0:
                ans = min(i - nums.index(nums[i]) + 1, ans)
    return ans
print(findShortestSubArray([1,2,2,3,1,4,2]))