def minimumDeletions(nums):
    if len(nums) < 3:
        return len(nums)
    max_ind = nums.index(max(nums)) + 1
    min_ind = nums.index(min(nums)) + 1
    if min_ind > len(nums) / 2 and max_ind > len(nums) / 2:
        return len(nums) - min(max_ind, min_ind) + 1
    return min(max(max_ind, min_ind), min(max_ind, min_ind) + len(nums) + 1 - max(max_ind, min_ind),
               len(nums) - min(min_ind, max_ind) + 1)
print(minimumDeletions([72956,-44432,78333,31358,-96449,-24776]))