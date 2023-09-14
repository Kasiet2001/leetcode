def maximumTop(nums, k):
    if len(nums) == 1:
        if k % 2 != 0:
            return -1
        else:
            return nums[0]
    if k <= 1:
        return nums[k]
    if k < len(nums):
        return max(max(nums[:k - 1]), nums[k])
    if k < len(nums) + 2:
        return max(nums[:k - 1])
    return max(nums)
print(maximumTop([1,2,1000000000], 2))