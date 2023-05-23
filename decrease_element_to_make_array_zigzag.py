def movesToMakeZigzag(nums):
    if len(nums) == 1:
        return 0
    even = odd = 0
    for i in range(1, len(nums), 2):
        minimum = 0
        if i + 1 < len(nums):
            minimum = min(nums[i - 1], nums[i + 1])
        else:
            minimum = nums[i - 1]
        if minimum <= nums[i]:
            odd += nums[i] - minimum + 1
    if nums[0] >= nums[1]:
        even += nums[0] - nums[1] + 1
    for i in range(2, len(nums), 2):
        minimum = 0
        if i + 1 < len(nums):
            minimum = min(nums[i - 1], nums[i + 1])
        else:
            minimum = nums[i - 1]
        if minimum <= nums[i]:
            even += nums[i] - minimum + 1
    return min(even, odd)
print(movesToMakeZigzag([9,6,1,6,2]))



