from bisect import bisect_left, insort
def findIndices(nums, indexDifference, valueDifference):
    ans = [-1, -1]
    mn = [float('inf'), -1]
    mx = [float('-inf'), -1]
    for i, v in enumerate(nums):
        if i >= indexDifference:
            if nums[i - indexDifference] < mn[0]:
                mn[0], mn[1] = nums[i - indexDifference], i - indexDifference
            if nums[i - indexDifference] > mx[0]:
                mx[0], mx[1] = nums[i - indexDifference], i - indexDifference
            if abs(v - mn[0]) >= valueDifference:
                return [mn[1], i]
            elif abs(v - mx[0]) >= valueDifference:
                return [mx[1], i]
    return ans
print(findIndices([1,2,3], 2, 4))