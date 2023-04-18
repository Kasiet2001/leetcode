def maximumCount(nums):
    pos, neg = 0, 0
    for i in nums:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    return max(pos, neg)
print(maximumCount([-2,-1,-1,1,2,3]))