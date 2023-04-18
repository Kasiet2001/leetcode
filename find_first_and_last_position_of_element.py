def searchRange(nums, target):
    if nums.count(target) == 0:
        return [-1, -1]
    elif nums.count(target) == 1:
        return [nums.index(target), nums.index(target)]
    else:
        return [nums.index(target), nums.index(target) + nums.count(target) - 1]
print(searchRange([], 0))