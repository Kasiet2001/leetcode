def canReduce(height, workerTimes, maxTime):
    totalReduction = 0
    for time in workerTimes:
        maxHeight = maxTime // time
        if maxHeight > 0:
            x = int(((-1 + (1 + 8 * maxHeight) ** 0.5) // 2))
            totalReduction += x
            if totalReduction >= height:
                return True
    return totalReduction >= height

def minNumberOfSeconds(mountainHeight, workerTimes):
    low, high = 0, mountainHeight * max(workerTimes) * (mountainHeight + 1) // 2

    while low < high:
        mid = (low + high) // 2
        if canReduce(mountainHeight, workerTimes, mid):
            high = mid
        else:
            low = mid + 1

    return low

print(minNumberOfSeconds(5, [1]))