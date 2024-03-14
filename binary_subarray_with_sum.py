def numSubarraysWithSum(nums, goal):
    d = {0: 1}
    ans = 0
    curr = 0
    for n in nums:
        curr += n
        if curr - goal in d:
            ans += d[curr - goal]
        if curr in d:
            d[curr] += 1
        else:
            d[curr] = 1
    return ans
print(numSubarraysWithSum([1,0,1,0,1], 2))