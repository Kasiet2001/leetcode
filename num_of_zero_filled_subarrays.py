def zeroFilledSubarray(nums):
    ans = total = 0
    for i in nums:
        if i == 0:
            total += 1
        else:
            total = 0
        ans += total
    return ans
print(zeroFilledSubarray([0,0,0,2,0,0]))