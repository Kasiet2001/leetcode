def getCommon(nums1, nums2):
    p1 = 0
    p2 = 0
    ans = float('inf')
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            ans = nums1[p1]
            break
        if nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
    return ans if ans != float('inf') else -1

