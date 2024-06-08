def checkSubarraySum(nums, k):
    pref = 0
    idx = {0: -1}
    for i in range(len(nums)):
        pref = (pref + nums[i]) % k
        if pref in idx:
            if i - idx[pref] > 1:
                return True
        else:
            idx[pref] = i
    return False
print(checkSubarraySum([1,2,12], 6))