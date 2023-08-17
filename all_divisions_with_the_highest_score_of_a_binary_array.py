from collections import defaultdict
def maxScoreIndices(nums):
    d = defaultdict(list)
    ones = sum(nums)
    zeros = 0
    d[ones].append(0)
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        else:
            ones -= 1
        d[zeros + ones].append(i + 1)
    m = max(d.keys())
    return d[m]
print(maxScoreIndices([1,1]))