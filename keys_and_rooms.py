def canVisitAllRooms(rooms):
    from collections import deque
    n = len(rooms)
    keys = deque([0])
    open = set()
    while keys and len(open) < n:
        key = keys.popleft()
        open.add(key)
        for r in rooms[key]:
            if r not in open:
                keys.append(r)
    return len(open) == n
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
