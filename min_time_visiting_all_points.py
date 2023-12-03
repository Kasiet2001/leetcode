def minTimeToVisitAllPoints(points):
    curr = points[0]
    ans = 0
    for i in range(1, len(points)):
        ans += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
    return ans
print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))