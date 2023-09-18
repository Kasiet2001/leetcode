from collections import defaultdict, deque
def longestEqualSubarray(nums, k):
    ind = defaultdict(deque)
    ans = 0
    for i, n in enumerate(nums):
        ind[n].append(i)
        while ind[n][-1] - ind[n][0] + 1 > len(ind[n]) + k:
            ind[n].popleft()
        ans = max(ans, len(ind[n]))
    return ans
print(longestEqualSubarray([1,3,2,3,1,3], 3))