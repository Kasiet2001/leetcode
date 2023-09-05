def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)
print(canBeEqual([3,7,9],  [3,7,11]))