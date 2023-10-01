from collections import Counter
def minOperations(nums):
    ans = 0
    num_of_nums = Counter(nums)
    for k, v in num_of_nums.items():
        if v == 1:
            return -1
        else:
            ans += (v - 1) // 3 + 1
    return ans
print(minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))