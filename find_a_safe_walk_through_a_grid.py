from collections import deque
def findSafeWalkDFS(grid, health):
    m, n = len(grid), len(grid[0])
    health -= grid[0][0]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(0, 0, health)])

    visited = set([(0, 0, health)])

    while queue:
        row, col, curr_health = queue.popleft()
        if row == m - 1 and col == n - 1 and curr_health > 0:
            return True

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < m and 0 <= new_col < n:
                new_health = curr_health - grid[new_row][new_col]

                if new_health > 0 and (new_row, new_col, new_health) not in visited:
                    visited.add((new_row, new_col, new_health))
                    queue.append((new_row, new_col, new_health))
    return False

print(findSafeWalkDFS([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1))
