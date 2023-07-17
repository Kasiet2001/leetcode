def distanceBetweenBusStops(distance, start, destination):
    if destination == start:
        return 0
    elif destination > start:
        dis = sum(distance[start:destination])
    else:
        dis = sum(distance[destination:start])
    c = sum(distance)
    if c - dis > dis:
        return dis
    return c - dis
print(distanceBetweenBusStops([1,2,3,4], 0, 1))