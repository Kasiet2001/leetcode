def findMatrix(nums):
    from collections import defaultdict
    n = defaultdict(int)
    for w in nums:
        n[w] += 1
    ans = []
    for i in range(max(n.values())):
        res = []
        for k, v in n.items():
            if v != 0:
                n[k] -= 1
                res.append(k)
        ans.append(res)
    return ans
print(findMatrix([1,3,4,1,2,3,1]))
