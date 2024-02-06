def findUnsortedSubarray(nums):
    n = len(nums)
    if n == 1:
        return 0
    left = 1
    while left < n - 1 and nums[left] > nums[left - 1]:
        left += 1
    mn = min(nums[left:])
    right = n - 2
    while right >= 0 and nums[right] < nums[right + 1]:
        right -= 1
    mx = max(nums[right::-1])
    i = 0
    while i < n and nums[i] <= mn:
        i += 1
    j = n - 1
    while j >= 0 and nums[j] >= mx:
        j -= 1

    return j - i + 1 if j - i > 0 else 0
print(findUnsortedSubarray([1,2,2,1]))


