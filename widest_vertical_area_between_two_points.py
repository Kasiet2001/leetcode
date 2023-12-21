def maxWidthOfVerticalArea(points):
    points = sorted(points, key=lambda x: x[0])
    ans = 0
    for i in range(1, len(points)):
        diff = points[i][0] - points[i - 1][0]
        ans = max(ans, diff)
    return ans
print(maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))