from collections import defaultdict
def subarraysDivByK(nums, k):
    pref_sum = 0
    pref_cnt = defaultdict(int)
    pref_cnt[0] = 1
    res = 0
    for num in nums:
        pref_sum += num
        remain = pref_sum % k
        res += pref_cnt[remain]
        pref_cnt[remain] += 1
    return res
print(subarraysDivByK([4,5,0,-2,-3,1], 5))