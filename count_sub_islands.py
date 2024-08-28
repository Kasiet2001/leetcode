from collections import deque
def countSubIslands(grid1, grid2):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans = 0
    def bfs(r, c, visited):
        rows = len(grid2)
        cols = len(grid2[0])
        q = deque()
        q.append((r, c))
        curr_island = [(r, c)]
        while q:
            curr_x, curr_y = q.popleft()
            for x, y in directions:
                next_x = curr_x + x
                next_y = curr_y + y
                if (0 <= next_x < rows and 0 <= next_y < cols
                    and (next_x, next_y) not in visited
                    and grid2[next_x][next_y] == 1):
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y))
                    curr_island.append((next_x, next_y))
        return curr_island

    def count_sub_islands(islands):
        for r, c in islands:
            if grid2[r][c] != grid1[r][c]:
                return 0
        return 1

    visited = set()
    for r in range(len(grid2)):
        for c in range(len(grid2[0])):
            islands = []
            if grid2[r][c] and (r, c) not in visited:
                visited.add((r, c))
                islands.extend(bfs(r, c, visited))
                ans += count_sub_islands(islands)

    return ans
print(countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))