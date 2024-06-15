import heapq
def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    projects = [(capital[i], profits[i]) for i in range(n)]
    projects.sort()
    i = 0
    maxHeap = []
    for _ in range(k):
        while i < n and projects[i][0] <= w:
            heapq.heappush(maxHeap, -projects[i][1])
            i += 1
        if not maxHeap:
            break
        w -= heapq.heappop(maxHeap)
    return w
print(findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))