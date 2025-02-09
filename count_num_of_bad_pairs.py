def countBadPairs(nums):
    diff_count = dict()
    ans = 0
    for i in range(len(nums)):
        diff = i - nums[i]
        good_pairs = diff_count.get(diff, 0)
        ans += i - good_pairs
        diff_count[diff] = good_pairs + 1
    return ans
print(countBadPairs([4,1,3,3]))
