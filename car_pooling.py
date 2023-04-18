def carPooling(trips, capacity):
    n = []
    for i, start, end in trips:
        n.append((start, i))
        n.append((end, -i))
    n.sort()
    p = 0
    for j in n:
        p += j[1]
        if p > capacity:
            return False
    return True
print(carPooling([[2,1,5],[3,3,7]], 4))