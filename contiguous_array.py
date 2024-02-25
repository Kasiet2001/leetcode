def findMaxLength(nums):
    ans = 0
    firstOccIdx = {}
    diff = 0
    for idx, num in enumerate(nums):
        if num == 0:
            diff -= 1
        else:
            diff += 1
        if diff == 0:
            ans = max(ans, idx + 1)
        elif diff not in firstOccIdx:
            firstOccIdx[diff] = idx
        else:
            ans = max(ans, idx - firstOccIdx[diff])
    return ans
print(findMaxLength([0,1,0,1]))