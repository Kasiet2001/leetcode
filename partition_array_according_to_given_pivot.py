def pivotArray(nums, pivot):
    ans = []
    c = 0
    for i in nums:
        if i < pivot:
            ans.insert(c, i)
            c += 1
        elif i == pivot:
            ans.append(pivot)
    for i in nums:
        if i > pivot:
            ans.append(i)
    return ans
print(pivotArray([-3,4,3,2], 2))