def repeatedNTimes(nums):
    n = sorted(nums)
    for i in range(len(nums) - 1):
        if n[i] == n[i + 1]:
            return n[i]
    return 0
print(repeatedNTimes([5,1,5,2,5,3,5,4]))