def maximumSetSize(nums1, nums2):
    n = len(nums1)
    n1 = set(nums1)
    n2 = set(nums2)
    common = n1.intersection(n2)
    res1 = min(len(n1) - len(common), n // 2)
    res2 = min(len(n2) - len(common), n // 2)
    return min(res1 + res2 + len(common), n)
print(maximumSetSize([1,2,1,2], [1,1,1,1]))