def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])
    ans = 0
    end_point = float('-inf')
    for i in points:
        if i[0] > end_point:
            ans += 1
            end_point = i[1]
    return ans
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
