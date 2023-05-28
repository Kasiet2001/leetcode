import bisect
def findRightInterval(intervals):
    start = {}
    for i, n in enumerate(intervals):
        start[n[0]] = i
    ans = [-1] * len(intervals)
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        ind = bisect.bisect_left(sorted_intervals, [interval[1]])
        if ind != len(intervals):
            ans[i] = start[sorted_intervals[ind][0]]
    return ans
print(findRightInterval([[1,4],[2,3],[3,4]]))