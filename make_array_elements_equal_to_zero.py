def countValidSelections(nums):
    right = sum(nums)
    left = 0
    res = 0
    for num in nums:
        if num == 0:
            if left == right:
                res += 2
            elif abs(left - right) == 1:
                res += 1
        left += num
        right -= num
    return res
print(countValidSelections([16,13,10,0,0,0,10,6,7,8,7]))