from collections import deque
def maxMoves(grid):
    dirs = [-1, 0, 1]
    M, N = len(grid), len(grid[0])
    q = deque()
    vis = [[False] * N for _ in range(M)]
    for i in range(M):
        vis[i][0] = True
        q.append((i, 0, 0))
    max_moves = 0
    while q:
        sz = len(q)

        for _ in range(sz):
            row, col, count = q.popleft()
            max_moves = max(max_moves, col)
            for dir in dirs:
                new_row, new_col = row + dir, col + 1
                if (
                    0 <= new_row < M
                    and 0 <= new_col < N
                    and not vis[new_row][new_col]
                    and grid[new_row][new_col] > grid[row][col]
                ):
                    vis[new_row][new_col] = True
                    q.append((new_row, new_col, count + 1))
    return max_moves
print(maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))