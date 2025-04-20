from collections import defaultdict
def countGood(nums, k):
    ans = 0
    sum_of_pairs = 0
    pairs = defaultdict(int)
    l = 0
    n = len(nums)
    for r in range(len(nums)):
        sum_of_pairs += pairs[nums[r]]
        pairs[nums[r]] += 1

        while sum_of_pairs >= k:
            ans += n - r
            pairs[nums[l]] -= 1
            sum_of_pairs -= pairs[nums[l]]
            l += 1
    return ans
print(countGood([3,1,4,3,2,2,4], 2))