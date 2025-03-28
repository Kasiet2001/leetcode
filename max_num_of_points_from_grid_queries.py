import heapq
def maxPoints(grid, queries):
    rows, cols = len(grid), len(grid[0])
    q = [(n, i) for i, n in enumerate(queries)]
    q.sort()
    min_heap = [(grid[0][0], 0, 0)]
    visited = set([(0, 0)])
    res = [0] * len(queries)
    points = 0
    for num, index in q:
        while min_heap and min_heap[0][0] < num:
            val, r, c = heapq.heappop(min_heap)
            points += 1
            neis = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neis:
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
        res[index] = points
    return res
print(maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]))