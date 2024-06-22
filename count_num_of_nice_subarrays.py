def numberOfSubarrays(nums, k):
    odd = 0
    ans = 0
    left, m = 0, 0
    for num in nums:
        if num % 2:
            odd += 1
        while odd > k:
            if nums[left] % 2:
                odd -= 1
            left += 1
            m = left
        if odd == k:
            while not nums[m] % 2:
                m += 1
            ans += m - left + 1
    return ans
print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))