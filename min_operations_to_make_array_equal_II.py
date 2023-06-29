def minOperations(nums1, nums2, k):
    inc_dec = ans = 0
    if k == 0:
        return -1 if nums1 != nums2 else 0
    for a, b in zip(nums1, nums2):
        diff = abs(a - b)
        if diff % k != 0:
            return -1
        inc_dec += a - b
        if a > b:
            ans += (a - b) // k
    return ans if inc_dec == 0 else -1
print(minOperations([4,3,1,4], [1,3,7,1], 3))
