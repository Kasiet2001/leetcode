from collections import defaultdict
def maxSubarrayLength(nums, k):
    freq = defaultdict(int)
    left = 0
    ans = 0
    for right, elem in enumerate(nums):
        freq[elem] += 1
        if freq[elem] > k:
            while freq[elem] > k:
                freq[nums[left]] -= 1
                left += 1
        ans = max(ans, right - left + 1)
    return ans
print(maxSubarrayLength([1,2,2,1,3], 1))

