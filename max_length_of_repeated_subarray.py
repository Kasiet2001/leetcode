def findLength(nums1, nums2):
    if nums1 == nums2:
        return len(nums1)
    num2 = ''.join([chr(x) for x in nums2])
    n = ''
    ans = 0
    for i in nums1:
        n += chr(i)
        if n in num2:
            ans = max(ans, len(n))
        else:
            n = n[1:]
    return ans
print(findLength([1,2,3,2,1], [3,2,1,4,7]))