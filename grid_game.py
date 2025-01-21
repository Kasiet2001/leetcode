def gridGame(grid):
    first_row = sum(grid[0])
    second_row = 0
    ans = float('inf')
    for i in range(len(grid[0])):
        first_row -= grid[0][i]
        ans = min(ans, max(first_row, second_row))
        second_row += grid[1][i]
    return ans
print(gridGame([[2,5,4],[1,5,1]]))