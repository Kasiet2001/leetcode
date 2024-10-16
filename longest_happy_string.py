import heapq
def longestDiverseString(a, b, c):
    pq = []
    if a > 0:
        heapq.heappush(pq, (-a, 'a'))
    if b > 0:
        heapq.heappush(pq, (-b, 'b'))
    if c > 0:
        heapq.heappush(pq, (-c, 'c'))
    res = []
    while pq:
        freq1, ch1 = heapq.heappop(pq)
        if len(res) >= 2 and res[-1] == ch1 and res[-2] == ch1:
            if not pq:
                break
            freq2, ch2 = heapq.heappop(pq)
            res.append(ch2)
            if freq2 + 1 < 0:
                heapq.heappush(pq, (freq2 + 1, ch2))
            heapq.heappush(pq, (freq1, ch1))
        else:
            freq1 += 1
            res.append(ch1)
            if freq1 < 0:
                heapq.heappush(pq, (freq1, ch1))
    return ''.join(res)
print(longestDiverseString(2,2,1))
