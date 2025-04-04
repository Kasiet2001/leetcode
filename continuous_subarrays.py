def continuousSubarrays(nums):
    freq = {}
    left = right = 0
    ans = 0
    while right < len(nums):
        freq[nums[right]] = freq.get(nums[right], 0) + 1
        while max(freq) - min(freq) > 2:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        ans += right - left + 1
        right += 1
    return ans
print(continuousSubarrays([5,4,2,4]))