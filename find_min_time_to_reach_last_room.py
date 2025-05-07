import heapq
def minTimeToReach(moveTime):
    rows, cols = len(moveTime), len(moveTime[0])
    minHeap = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0))
    ans = float('inf')
    while minHeap:
        time, row, col = heapq.heappop(minHeap)
        if row == rows - 1 and col == cols - 1:
            ans = min(ans, time)
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                new_time = max(moveTime[new_row][new_col], time) + 1
                heapq.heappush(minHeap, (new_time, new_row, new_col))
                visited.add((new_row, new_col))
    return ans
print(minTimeToReach([[0,0,0],[0,0,0]]))