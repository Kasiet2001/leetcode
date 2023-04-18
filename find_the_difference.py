def findDifference(nums1, nums2):
    n1 = list(set([i for i in nums1 if i not in nums2]))
    n2 = list(set([i for i in nums2 if i not in nums1]))
    return [n1, n2]

def findDifference(nums1, nums2):
    s = (set(nums1 + nums2)) - set(nums2)
    t = (set(nums1 + nums2)) - set(nums1)
    return ([list(s), list(t)])
print(findDifference([1,2,3,3], [1,1,2,2]))