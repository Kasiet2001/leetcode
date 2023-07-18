from collections import Counter
def minimumIndex(nums):
    n = len(nums)
    d, right= Counter(nums).most_common()[0]
    left = 0
    for i in range(n):
        if nums[i] == d:
            left += 1
            right -= 1
        if left * 2 > i + 1 and right * 2 > n - (i + 1):
            return i
    return -1
print(minimumIndex([1,2,2,2]))