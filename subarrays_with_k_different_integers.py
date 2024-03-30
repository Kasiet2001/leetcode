def subarraysWithKDistinct(nums, k):
    if k == 0:
        return 0
    def solve(nums,k):
        ans = 0
        freq = {}
        diff = 0
        left = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    freq.pop(nums[left])
                left += 1
            ans += (right - left + 1)
        return ans
    return solve(nums, k) - solve(nums, k - 1)
print(subarraysWithKDistinct([1,2,1,2,3], 2))