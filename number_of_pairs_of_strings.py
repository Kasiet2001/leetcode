def numOfPairs(nums, target):
    total = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                total += 1
            if nums[j] + nums[i] == target:
                total += 1
    return total
print(numOfPairs(["1","1","1"],"11"))