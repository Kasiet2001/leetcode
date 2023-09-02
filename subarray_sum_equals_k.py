def subarraySum(nums, k):
    d = {0: 1}
    ans = 0
    curr = 0
    for n in nums:
        curr += n
        if curr - k in d:
            ans += d[curr - k]
        if curr in d:
            d[curr] += 1
        else:
            d[curr] = 1
    return ans
print(subarraySum([1,1,1], 2))