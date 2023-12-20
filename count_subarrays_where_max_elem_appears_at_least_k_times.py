def countSubarrays(nums, k):
    n = len(nums)
    ans = 0
    maximum = max(nums)
    count = 0
    left = 0
    for right in range(n):
        if nums[right] == maximum:
            count += 1
        if count >= k:
            while count >= k:
                ans += n - right
                if nums[left] == maximum:
                    count -= 1
                left += 1
    return ans
print(countSubarrays([1,0,3,8,8,8,7,8,7], 2))
