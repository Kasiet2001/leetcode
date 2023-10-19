def countElements(nums):
    nums.sort()
    ans = 0
    sm, gr = nums[0], nums[-1]
    for i in nums:
        if i != sm and i != gr:
            ans += 1
    return ans
print(countElements([-3,3,3,90]))