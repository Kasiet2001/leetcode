def shuffle(nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[n + i])
    return ans
print(shuffle([1,2,3,4,4,3,2,1], 4))