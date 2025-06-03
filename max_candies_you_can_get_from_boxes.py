from collections import deque
def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    n = len(candies)
    can_open = [status[i] == 1 for i in range(n)]
    has_box, used = [False] * n, [False] * n
    q = deque()
    ans = 0
    for box in initialBoxes:
        has_box[box] = True
        if can_open[box]:
            ans += candies[box]
            q.append(box)
            used[box] = True
    while q:
        box = q.pop()
        for key in keys[box]:
            can_open[key] = True
            if not used[key] and has_box[key]:
                q.append(key)
                used[key] = True
                ans += candies[key]
        for b in containedBoxes[box]:
            has_box[b] = True
            if not used[b] and can_open[b]:
                q.append(b)
                used[b] = True
                ans += candies[b]
    return ans
print(maxCandies([1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0]))
