def jump(nums):
    res = 0
    max_j = 0
    end = 0
    for i, num in enumerate(nums[:-1]):
        max_j = max(max_j, i + num)
        if i == end:
            res += 1
            end = max_j
    return res
print(jump([2,3,1,1,4]))