from bisect import bisect_right
def longestObstacleCourseAtEachPosition(obstacles):
    n, ans = [], []
    for i in obstacles:
        m = bisect_right(n, i)
        if m == len(n):
            n.append(i)
        else:
            n[m] = i
        ans.append(m + 1)
    return ans
print(longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))