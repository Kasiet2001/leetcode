def checkArithmeticSubarrays(nums, l, r):
    b = 0
    ans = []
    for i in range(len(l)):
        sub = sorted(nums[l[i]: r[i] + 1])
        if len(sub) == 1 or len(sub) == 2:
            ans.append(True)
            continue
        for j in range(1, len(sub) - 1):
            if sub[j - 1] - sub[j] == sub[j] - sub[j + 1]:
                b = 1
            else:
                b = 0
                break
        if b == 1:
            ans.append(True)
        else:
            ans.append(False)
    return ans
print(checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))
