def busyStudent(startTime, endTime, queryTime):
    ans = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime <= endTime[i]:
            ans += 1
    return ans
print(busyStudent([1,2,3], [3,2,7], 4))