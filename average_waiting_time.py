def averageWaitingTime(customers):
    start = 0
    time = 0
    for a, t in customers:
        start = max(start, a) + t
        time += start - a
    return time / len(customers)
print(averageWaitingTime([[1,2],[2,5],[4,3]]))