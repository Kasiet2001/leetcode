from collections import defaultdict
def maxSum(nums):
    d = defaultdict(list)
    for i in nums:
        d[max(str(i))].append(i)
    ans = -1
    for k, v in d.items():
        v.sort()
        if len(v) > 1 and ans < v[-1] + v[-2]:
            ans = v[-1] + v[-2]
    return ans
print(maxSum([1,2,3,4]))