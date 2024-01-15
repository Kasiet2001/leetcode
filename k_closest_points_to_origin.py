import heapq
def kClosest(points, k):
    min_p = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        min_p.append([dist, [x, y]])
    heapq.heapify(min_p)
    ans = []
    while len(ans) < k:
        n = heapq.heappop(min_p)
        ans.append(n[1])
    return ans
print(kClosest([[3,3],[5,-1],[-2,4]], 2))