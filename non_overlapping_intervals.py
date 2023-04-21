def eraseOverlapIntervals(intervals):
    n = float('-inf')
    ans = 0
    for s, e in sorted(intervals, key=lambda x: x[1]):
        if s >= n:
            n = e
        else:
            ans += 1
    return ans
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))