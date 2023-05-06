def numSubseq(nums, target):
    nums.sort()
    ans = 0
    l, r = 0, len(nums) - 1
    mod = 10 ** 9 + 7
    while l <= r:
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            ans += pow(2, r - l, mod)
            l += 1
    return ans % mod
print(numSubseq([3,3,6,8], 10))