def eliminateMaximum(dist, speed):
    ans = 0
    time = sorted([i / j for i, j in zip(dist, speed)])
    for i in range(len(dist)):
        if time[i] <= i:
            return ans
        ans += 1
    return ans
print(eliminateMaximum([4,2,3], [2,1,1]))