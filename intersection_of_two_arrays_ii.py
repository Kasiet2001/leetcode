def intersect(nums1, nums2):
    i = []
    for n in set(nums1):
        if n in nums2:
            i.extend([n] * min(nums1.count(n), nums2.count(n)))
    return i
print(intersect([4,9,5],[9,4,9,8,4]))