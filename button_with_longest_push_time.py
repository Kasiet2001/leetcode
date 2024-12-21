def buttonWithLongestTime(events):
    res, time = events[0]
    for i in range(1, len(events)):
        t = events[i][1] - events[i - 1][1]
        if time < t:
            time = t
            res = events[i][0]
        elif time == t:
            res = min(res, events[i][0])
    return res
print(buttonWithLongestTime([[9,4],[19,5],[2,8],[3,11],[2,15]]))
