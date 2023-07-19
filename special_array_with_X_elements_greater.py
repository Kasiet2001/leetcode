import bisect
def specialArray(nums):
    nums.sort()
    for i in range(max(nums) + 1):
        x = len(nums) - bisect.bisect_left(nums, i)
        if x == i:
            return i
    return -1
print(specialArray([3,5]))