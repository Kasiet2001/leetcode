def arrayChange(nums, operations):
    val_idx = {val: idx for idx, val in enumerate(nums)}
    for i, j in operations:
        nums[val_idx[i]] = j
        val_idx[j] = val_idx[i]
    return nums
print(arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]]))