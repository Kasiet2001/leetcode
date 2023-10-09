def minProcessingTime(processorTime, tasks):
    tasks.sort()
    processorTime.sort(reverse=True)
    ans = 0
    ind = 3
    for i in processorTime:
        ans = max(ans, i + tasks[ind])
        ind += 4
    return ans
print(minProcessingTime([8,10], [2,2,3,1,8,7,4,5]))