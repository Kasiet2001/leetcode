def rotate(nums, k):
    if k == 0:
        return nums
    k = k % len(nums)
    l = len(nums)
    nums[l - k:], nums[:l - k] = nums[:l - k], nums[l - k:]
    return nums
print(rotate([1,2,3,4,5,6,7], 3))