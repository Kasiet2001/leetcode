from collections import defaultdict
def maximumSum(nums):
    d = defaultdict(list)
    for n in nums:
        summ = 0
        num = n
        while num:
            summ += num % 10
            num //= 10
        d[summ].append(n)
    ans = -1
    for v in d.values():
        if len(v) > 1:
            v = sorted(v, reverse=True)
            ans = max(ans, v[0] + v[1])
    return ans
print(maximumSum([18,43,36,13,7]))