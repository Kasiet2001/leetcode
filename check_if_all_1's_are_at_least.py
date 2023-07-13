def kLengthApart(nums, k):
    if 1 not in nums:
        return True
    prev = nums.index(1)
    for i in range(prev + 1, len(nums)):
        if nums[i] == 1:
            if i - prev <= k:
                return False
            prev = i
    return True
print(kLengthApart([1,0,0,0,1,0,0,1], 2))