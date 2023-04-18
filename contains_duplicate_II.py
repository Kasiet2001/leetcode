def containsNearbyDuplicate(nums, k):
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            diff = i - d[num]
            if diff <= k:
                return True
        d[num] = i
    return False
print(containsNearbyDuplicate([1,2,3,1], 3))