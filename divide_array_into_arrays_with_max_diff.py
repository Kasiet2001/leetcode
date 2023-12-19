def divideArray(nums, k):
    nums.sort()
    ans = []
    for i in range(0, len(nums), 3):
        if nums[i + 2] - nums[i] <= k:
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        else:
            return []
    return ans
print(divideArray([1,3,4,8,7,9,3,5,1], 2))
