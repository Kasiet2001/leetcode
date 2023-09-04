def maxDistance(nums1, nums2):
    i = 0
    j = 0
    ans = 0
    l1, l2 = len(nums1), len(nums2)
    while i < l1 and j < l2:
        if nums2[j] < nums1[i]:
            i += 1
        else:
            ans = max(ans, j - i)
            j += 1
    return ans
print(maxDistance([55,30,5,4,2], [100,20,10,10,5]))
