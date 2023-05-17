def findMinDifference(timePoints):
    minutes = []
    for i in timePoints:
        if i[:2] == '00' and i[3:] == '00':
            minutes.append(24 * 60 + int(i[3:]))
        else:
            minutes.append(int(i[:2]) * 60 + int(i[3:]))
    minutes.sort()
    maximum = 24 * 60
    ans = maximum
    for i in range(1, len(minutes)):
        ans = min(ans, minutes[i] - minutes[i - 1])
    ans = min(ans, (minutes[0] - minutes[-1]) % maximum)
    return ans
print(findMinDifference(["05:31","22:08","00:35"]))