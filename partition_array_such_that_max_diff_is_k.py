def partitionArray(nums, k):
    nums.sort()
    ans = 1
    ind = 0
    for i in range(len(nums)):
        if nums[i] - nums[ind] > k:
            ans += 1
            ind = i
    return ans
print(partitionArray([2,2,4,5], 0))