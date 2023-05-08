from bisect import bisect
def lengthOfLIS(nums):
    n = []
    for i in nums:
        ind = bisect(n, i)
        if i not in n:
            if len(n) == ind:
                n.append(i)
            else:
                n[ind] = i
    return len(n)
print(lengthOfLIS([7,7,7,7,7,7,7]))
