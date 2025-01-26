def countPartitions(nums):
    total = sum(nums)
    res = 0
    curr = 0
    for i in range(len(nums) - 1):
        curr += nums[i]
        total -= nums[i]
        if (curr - total) % 2 == 0:
            res += 1
    return res
print(countPartitions([1,2,2]))