def minSum(nums1, nums2):
    sum1 = sum(nums1) + nums1.count(0)
    sum2 = sum(nums2) + nums2.count(0)
    if (nums1.count(0) == 0 and sum2 > sum1) or (nums2.count(0) == 0 and sum1 > sum2):
        return -1
    return max(sum1, sum2)
print(minSum([2,0,2,0], [1,4]))