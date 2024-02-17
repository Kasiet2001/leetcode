import heapq
def furthestBuilding(heights, bricks, ladders):
    p = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        bricks -= diff
        heapq.heappush(p, -diff)
        if bricks < 0:
            bricks += -heapq.heappop(p)
            ladders -= 1
        if ladders < 0:
            return i
    return len(heights) - 1
print(furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))