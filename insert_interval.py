def insert(intervals, newInterval):
    ans = []
    for i, n in enumerate(intervals):
        if newInterval[1] < n[0]:
            ans.append(newInterval)
            return ans + intervals[i:]
        elif newInterval[0] > n[1]:
            ans.append(n)
        else:
            newInterval = [min(newInterval[0], n[0]), max(newInterval[1], n[1])]
    ans.append(newInterval)
    return ans
print(insert([[1,3],[6,9]], [2,5]))