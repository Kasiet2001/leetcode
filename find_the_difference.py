def findDifference(nums1, nums2):
    return ([list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))])
print(findDifference([1,2,3,3], [1,1,2,2]))