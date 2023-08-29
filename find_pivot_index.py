def pivotIndex(nums):
    sum_left = 0
    sum_right = sum(nums)
    for i in range(len(nums)):
        sum_right -= nums[i]
        if sum_left == sum_right:
            return i
        sum_left += nums[i]
    return -1
print(pivotIndex([1,7,3,6,5,6]))
