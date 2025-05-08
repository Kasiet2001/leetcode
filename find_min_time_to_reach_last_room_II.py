import heapq
def minTimeToReach(moveTime):
    rows, cols = len(moveTime), len(moveTime[0])
    ans = float('inf')
    visited = set()
    visited.add((0, 0))
    minHeap = [(0, 0, 0, True)]
    while minHeap:
        time, row, col, even = heapq.heappop(minHeap)
        if row == rows - 1 and col == cols - 1:
            ans = min(ans, time)
            return ans
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                n = 1 if even else 2
                new_time = max(moveTime[new_row][new_col], time) + n
                visited.add((new_row, new_col))
                heapq.heappush(minHeap, (new_time, new_row, new_col, False if even else True))
print(minTimeToReach([[0,0,0,0],[0,0,0,0]]))

