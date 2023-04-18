def totalCost(costs, k, candidates):
    import heapq
    if len(costs) <= 2 * candidates:
        return sum(sorted(costs)[:k])
    left = costs[:candidates]
    right = costs[-candidates:]
    heapq.heapify(left)
    heapq.heapify(right)
    i = candidates
    j = len(costs) - candidates - 1
    res = 0
    while i <= j and k > 0:
        if left[0] <= right[0]:
            res += heapq.heappop(left)
            heapq.heappush(left, costs[i])
            i += 1
        else:
            res += heapq.heappop(right)
            heapq.heappush(right, costs[j])
            j -= 1
        k -= 1
    if k != 0:
        temp = left + right
        heapq.heapify(temp)
        for i in range(k):
            res += heapq.heappop(temp)
    return res
print(totalCost([50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], 7, 12))