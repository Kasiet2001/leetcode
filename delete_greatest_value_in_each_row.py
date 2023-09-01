def deleteGreatestValue(grid):
    for i in range(0, len(grid)):
        grid[i].sort(reverse=True)
    ans = 0
    for i in range(len(grid[0])):
        max_value = 0
        for j in range(len(grid)):
            max_value = max(max_value, grid[j][i])
        ans += max_value
    return ans
print(deleteGreatestValue([[1,2,4],[3,3,1]]))