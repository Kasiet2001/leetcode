def latestTimeCatchTheBus(buses, passengers, capacity):
    passengers.sort()
    ind = 0
    buses.sort()
    for i in buses:
        cap = capacity
        while ind < len(passengers) and passengers[ind] <= i and cap > 0:
            ind += 1
            cap -= 1
    t = i if cap > 0 else passengers[ind - 1]
    while t in passengers:
        t -= 1
    return t
print(latestTimeCatchTheBus([3],[2,4], 2))