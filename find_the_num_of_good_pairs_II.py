from collections import defaultdict
def numberOfPairs(nums1, nums2, k):
    mp = defaultdict(int)
    for m in nums2:
        mp[m * k] += 1
    res = 0
    for n in nums1:
        for i in range(1, int(n ** 0.5) + 1):
            if n % i:
                continue
            res += mp[i]
            if i != (n // i):
                res += mp[n // i]
    return res
print(numberOfPairs([1,2,4,12], [2,4], 3))
