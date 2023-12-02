def countCompleteSubarrays(nums):
    s = set(nums)
    ans = 0
    for i in range(len(nums)):
        sub_set = set()
        for j in range(i, len(nums)):
            sub_set.add(nums[j])
            if sub_set == s:
                ans += 1
    return ans
print(countCompleteSubarrays([1,3,1,2,2]))