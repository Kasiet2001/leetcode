from math import gcd
def minOperations(nums):
    ones = nums.count(1)
    if ones:
        return len(nums) - ones
    d = float('inf')
    for i in range(len(nums)):
        g = nums[i]
        for j in range(i + 1, len(nums)):
            g = gcd(g, nums[j])
            if g == 1:
                d = min(d, j - i)
    return -1 if d == float('inf') else len(nums) - 1 + d
print(minOperations([2,6,3,4]))