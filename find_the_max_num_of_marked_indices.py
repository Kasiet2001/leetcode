def maxNumOfMarkedIndices(nums):
    nums.sort()
    middle = len(nums) // 2
    i, j = 0, middle
    ans = 0
    while i < middle and j < len(nums):
        if 2 * nums[i] <= nums[j]:
            ans += 2
            i += 1
        j += 1
    return ans
print(maxNumOfMarkedIndices([3,5,2,4]))