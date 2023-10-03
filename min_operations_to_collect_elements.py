def minOperations(nums, k):
    k = [i for i in range(1, k + 1)]
    ans = 0
    for i in range(len(nums) - 1, -1, -1):
        if len(k) > 0:
            if nums[i] in k:
                k.remove(nums[i])
        else:
            break
        ans += 1
    return ans
print(minOperations([3,1,5,4,2], 2))