def moveZeroes(nums):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
    return nums
print(moveZeroes([0,1,0,3,12]))