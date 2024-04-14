def minRectanglesToCoverPoints(points, w):
    points.sort()
    ans = 1
    point = points[0][0]
    for x, y in points:
        if x - point > w:
            point = x
            ans += 1
    return ans
print(minRectanglesToCoverPoints([[2,3],[1,2]], 0))