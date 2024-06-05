def countDays(days, meetings):
    meetings.sort()
    ans = 0
    curr = 0
    for s, e in meetings:
        if s > curr:
            ans += s - curr - 1
        if curr < e:
            curr = e
    return ans + days - curr
print(countDays(10, [[5,7],[1,3],[9,10]]))