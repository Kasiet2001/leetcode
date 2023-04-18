def goodIndices(nums, k):
    n = len(nums)
    non_dec, non_inc = [1] * n, [1] * n
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            non_inc[i] = non_inc[i - 1] + 1
        if nums[i] >= nums[i - 1]:
            non_dec[i] = non_dec[i - 1] + 1
    return non_dec, non_inc
print(goodIndices([253747,459932,263592,354832,60715,408350,959296], 2))