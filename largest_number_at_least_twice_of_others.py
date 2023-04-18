def dominantIndex(nums):
    index_largest = nums.index(max(nums))
    return index_largest if sorted(nums)[-2] * 2 <= nums[index_largest] else -1
print(dominantIndex([0,0,0,1]))