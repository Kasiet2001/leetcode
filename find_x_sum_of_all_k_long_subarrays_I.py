from collections import defaultdict
def findXSum(nums, k, x):
    ans = []
    freq = defaultdict(int)
    idx = 0
    left = 0
    while idx < len(nums):
        while idx - left < k:
            freq[nums[idx]] += 1
            idx += 1
        most_frequent = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
        total = 0
        for i in range(min(x, len(most_frequent))):
            total += most_frequent[i][0] * most_frequent[i][1]
        ans.append(total)
        freq[nums[left]] -= 1
        left += 1
    return ans
print(findXSum([9,2,2], 3, 3))


