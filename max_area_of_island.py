def maxAreaOfIsland(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs_explore(row, col, curr_area):
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
            return curr_area

        curr_area += grid[row][col]
        grid[row][col] = 0

        for dr, dc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            curr_area = dfs_explore(dr, dc, curr_area)
        return curr_area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                max_area = max(max_area, dfs_explore(r, c, 0))

    return max_area
print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
