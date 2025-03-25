def checkValidCuts(n, rectangles):
    x = []
    y = []
    for sx, sy, ex, ey in rectangles:
        x.append([sx, ex])
        y.append([sy, ey])
    def check(intervals):
        intervals.sort()
        sections = 0
        max_end = intervals[0][1]
        for start, end in intervals:
            if max_end <= end:
                sections += 1
            max_end = max(max_end, end)
        return sections >= 2
    return check(x) or check(y)
print(checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))