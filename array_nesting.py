def arrayNesting(nums):
    l = len(nums)
    visited = [0] * l
    for i in range(l):
        ind = i
        n = 0
        while not visited[ind]:
            visited[ind] = n
            ind = nums[ind]
            n += 1
    return visited
print(arrayNesting([5,4,0,3,1,6,2]))