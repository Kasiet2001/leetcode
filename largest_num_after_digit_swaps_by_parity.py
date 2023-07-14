import heapq
def largestInteger(num):
    odd = []
    even = []
    res = []
    string = str(num)
    for i in string:
        if int(i) % 2 == 0:
            even.append(-int(i))
        else:
            odd.append(-int(i))
    heapq.heapify(odd)
    heapq.heapify(even)
    for j in string:
        if int(j) % 2 == 0:
            res.append(str(-heapq.heappop(even)))
        else:
            res.append(str(-heapq.heappop(odd)))
    return int(''.join(res))
print(largestInteger(1234))