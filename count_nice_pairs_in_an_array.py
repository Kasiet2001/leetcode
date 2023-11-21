from collections import defaultdict
def countNicePairs(nums):
    ans = 0
    d = defaultdict(int)
    for i in nums:
        rev = str(i)[::-1]
        diff = i - int(rev)
        ans += d[diff]
        d[diff] += 1
    return ans
print(countNicePairs([13,10,35,24,76]))