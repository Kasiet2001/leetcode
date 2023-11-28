def maxScore(nums):
    nums.sort(reverse=True)
    total = 0
    for i, v in enumerate(nums):
        total += v
        if total <= 0:
            return i
    return len(nums)
