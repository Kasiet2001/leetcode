def canMakeSquare(grid):
    color = grid[1][1]
    squares = [
        [grid[0][0], grid[0][1], grid[1][0], grid[1][1]],
        [grid[0][1], grid[0][2], grid[1][1], grid[1][2]],
        [grid[1][0], grid[1][1], grid[2][0], grid[2][1]],
        [grid[1][1], grid[1][2], grid[2][1], grid[2][2]],
    ]
    for i in squares:
        if i.count(color) in (1, 3, 4):
            return True
    return False
print(canMakeSquare([["B","B","B"],["B","B","B"],["B","B","B"]]))