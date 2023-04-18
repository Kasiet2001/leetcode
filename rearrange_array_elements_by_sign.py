def rearrangeArray(nums):
    l = [0] * len(nums)
    p = 0
    n = 1
    for i in nums:
        if i > 0:
            l[p] = i
            p += 2
        else:
            l[n] = i
            n += 2
    return l
print(rearrangeArray([3,1,-2,-5,2,-4]))