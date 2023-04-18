def findKthLargest(nums, k):
    from random import choice
    pivot = choice(nums)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]
    L, M = len(left), len(mid)
    if k <= L:
        return findKthLargest(left, k)
    elif k > L + M:
        return findKthLargest(right, k - L - M)
    else:
        return mid[0]
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))