import heapq
def minGroups(intervals):
    min_heap = []
    intervals.sort()
    for s, e in intervals:
        if min_heap and min_heap[0] < s:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, e)
    return len(min_heap)
print(minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
