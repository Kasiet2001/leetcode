from collections import deque
def advantageCount(nums1, nums2):
    n = len(nums1)
    ans = [0] * n

    p = deque(sorted(nums1))
    q = sorted(range(n), key=lambda x: nums2[x], reverse=True)
    for idx in q:
        if p[-1] > nums2[idx]:
            ans[idx] = p.pop()
        else:
            ans[idx] = p.popleft()

    return ans
print(advantageCount([12,24,8,32], [13,25,32,11]))