def colorTheArray(n, queries):
    ans = []
    nums = [0] * n
    count = 0
    for i in queries:
        ind, color = i
        if ind - 1 >= 0 and nums[ind] != 0 and nums[ind - 1] == nums[ind]:
            count -= 1
        if ind + 1 < n and nums[ind] != 0 and nums[ind + 1] == nums[ind]:
            count -= 1
        nums[ind] = color
        if ind - 1 >= 0 and nums[ind] != 0 and nums[ind - 1] == nums[ind]:
            count += 1
        if ind + 1 < n and nums[ind] != 0 and nums[ind + 1] == nums[ind]:
            count += 1
        ans.append(count)
    return ans
print(colorTheArray(4,[[0,2],[1,2],[3,1],[1,1],[2,1]]))

