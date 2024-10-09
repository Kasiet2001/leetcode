def maximumTotalSum(maximumHeight):
    maximumHeight.sort(reverse=True)
    for i in range(1, len(maximumHeight)):
        maximumHeight[i] = min(maximumHeight[i], maximumHeight[i - 1] - 1)
        if maximumHeight[i] == 0:
            return -1
    return -1 if len(set(maximumHeight)) < len(maximumHeight) else sum(maximumHeight)
print(maximumTotalSum([2,2,1]))