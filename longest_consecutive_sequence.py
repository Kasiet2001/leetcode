def longestConsecutive(nums):
    c = []
    nums = sorted(set(nums))
    l = 1
    if len(nums) == 0:
        return 0
    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            l += 1
            c.append(l)
        else:
            l = 1
    return max(c) if len(c) != 0 else 1
print(longestConsecutive([1, 3]))
