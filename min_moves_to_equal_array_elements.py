def minMoves(nums):
    nums.sort()
    ans = 0
    min_elem = nums[0]
    for i in range(1, len(nums)):
        ans += nums[i] - min_elem
    return ans