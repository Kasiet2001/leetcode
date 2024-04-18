def islandPerimeter(grid):
    row = len(grid)
    colm = len(grid[0])
    ans = 0
    for i in range(row):
        for j in range(colm):
            if grid[i][j] == 1:
                ans += 4
                if i > 0 and grid[i - 1][j] == 1:
                    ans -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    ans -= 2
    return ans
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))