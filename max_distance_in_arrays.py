def maxDistance(arrays):
    curr_min = arrays[0][0]
    curr_max = arrays[0][-1]
    res = 0
    for i in range(1, len(arrays)):
        res = max(res, abs(arrays[i][-1] - curr_min), abs(curr_max - arrays[i][0]))
        curr_min = min(arrays[i][0], curr_min)
        curr_max = max(arrays[i][-1], curr_max)
    return res
print(maxDistance([[1,2,3],[4,5],[1,2,3]]))