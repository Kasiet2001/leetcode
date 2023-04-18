import heapq
def avoidFlood(rains):
    from collections import defaultdict
    dic = defaultdict(list)
    to_empty = []
    ans = [-1] * len(rains)
    full = set([])
    for day, lake in enumerate(rains):
        dic[lake].append(day)
    for i in range(len(rains)):
        lake = rains[i]
        if lake in full:
            return []
        full.add(lake)
        dic[lake].pop(0)
        if dic[lake]:
            heapq.heappush(to_empty, dic[lake][0])
        else:
            if to_empty:
                ans[i] += rains[heapq.heappop(to_empty)]
                full.remove(ans[i])
            else:
                ans[i] = 1
    return ans
print(avoidFlood([1,2,0,0,2,1]))