from collections import defaultdict
def isGood(nums):
    base = len(nums) - 1
    d = defaultdict(int)
    for i in nums:
        if i > base:
            return False
        d[i] += 1
        if i != base and d[i] > 1:
            return False
    if d[base] != 2:
        return False
    return True
print(isGood([1, 3, 3, 2]))