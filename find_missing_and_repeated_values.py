def findMissingAndRepeatedValues(grid):
    a, b = 0, 0
    nums = []
    for i in grid:
        nums.extend(i)
    n = len(nums) + 1
    for j in range(1, n):
        if j not in nums:
            b = j
        if nums.count(j) > 1:
            a = j
    return [a, b]
print(findMissingAndRepeatedValues([[1,3],[2,2]]))
