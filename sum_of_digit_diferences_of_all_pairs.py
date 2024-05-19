from collections import defaultdict
def sumDigitDifferences(nums):
    pos = defaultdict(int)
    digits_in_pos = defaultdict(int)
    ans = 0
    for num in nums:
        n = str(num)
        for i, d in enumerate(n):
            digits_in_pos[i] += 1
            pos[(i, d)] += 1
            ans += digits_in_pos[i] - pos[(i, d)]
    return ans
print(sumDigitDifferences([13,23,12]))