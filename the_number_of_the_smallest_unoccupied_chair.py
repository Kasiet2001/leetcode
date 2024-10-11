import heapq
def smallestChair(times, targetFriend):
    times = [(t[0], t[1], i) for i, t in enumerate(times)]
    times.sort()
    available_chairs = [i for i in range(len(times))]
    used_chairs = []
    for a, l, i in times:
        while used_chairs and used_chairs[0][0] <= a:
            leave, chair = heapq.heappop(used_chairs)
            heapq.heappush(available_chairs, chair)
        chair = heapq.heappop(available_chairs)
        heapq.heappush(used_chairs, (l, chair))
        if i == targetFriend:
            return chair

print(smallestChair([[3,10],[1,5],[2,6]], 0))