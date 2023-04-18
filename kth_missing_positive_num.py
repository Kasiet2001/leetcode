def findKthPositive(arr, k) -> int:
    nums = []
    n = 1
    while len(nums) != k:
        if n not in arr:
            nums.append(n)
        n += 1
    return nums[-1]
print(findKthPositive([1,2,3,4], 2))