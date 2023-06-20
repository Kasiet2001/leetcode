def getAverages(nums, k):
    n = len(nums)
    m = 2 * k + 1
    ans = [-1] * n
    if n < m:
        return ans
    pref = [0]
    for i in range(n):
        pref.append(pref[-1] + nums[i])
    for i in range(k, n - k):
        ans[i] = (pref[i + k + 1] - pref[i - k]) // m
    return ans
print(getAverages([7,4,3,9,1,8,5,2,6], 3))