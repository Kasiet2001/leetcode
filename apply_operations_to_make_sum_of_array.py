from math import ceil
def minOperations(k):
    ans = k + 1
    for i in range(1, k + 1):
        n = ceil(k / i)
        curr = (i - 1) + (n - 1)
        ans = min(ans, curr)
    return ans
print(minOperations(11))