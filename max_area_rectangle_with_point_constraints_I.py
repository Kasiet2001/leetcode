def maxRectangleArea(points):
    point_set = set(map(tuple, points))
    max_area = -1

    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            if x1 != x2 and y1 != y2:
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    x_min, x_max = min(x1, x2), max(x1, x2)
                    y_min, y_max = min(y1, y2), max(y1, y2)
                    valid = True

                    for px, py in points:
                        if x_min <= px <= x_max and y_min <= py <= y_max:
                            if (px, py) not in {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}:
                                valid = False
                                break

                    if valid:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        max_area = max(max_area, area)

    return max_area


print(maxRectangleArea([[1,1],[1,3],[3,1],[3,3]]))
