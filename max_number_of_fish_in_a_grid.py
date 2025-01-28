def findMaxFish(grid):
    ans = 0

    def bfs(seen, row, col):
        q = [(row, col)]
        row_directions = [0, 0, 1, -1]
        col_directions = [1, -1, 0, 0]
        curr = 0
        seen[row][col] = True
        while q:
            r, c = q.pop(0)
            curr += grid[r][c]
            for i in range(4):
                new_r = r + row_directions[i]
                new_c = c + col_directions[i]
                if (
                        0 <= new_r < rows and 0 <= new_c < cols
                and grid[new_r][new_c] and not seen[new_r][new_c]):
                    q.append((new_r, new_c))
                    seen[new_r][new_c] = True
        return curr

    rows = len(grid)
    cols = len(grid[0])
    seen = [[False] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                ans = max(ans, bfs(seen, r, c))
    return ans
print(findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))