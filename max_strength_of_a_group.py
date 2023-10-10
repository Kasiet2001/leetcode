from math import prod
def maxStrength(nums):
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    neg = [i for i in nums if i < 0]
    pos = [i for i in nums if i > 0]
    if not neg and not pos:
        return 0
    if len(neg) % 2:
        if neg[:-1]:
            n = prod(neg[:-1])
        else:
            n = 0
    else:
        n = prod(neg)
    if pos:
        p = prod(pos)
    else:
        p = 0
    return p * n
print(maxStrength([0, -5, 0]))