import collections
import heapq
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize:
        return False
    freq = collections.defaultdict(int)
    for num in hand:
        freq[num] += 1
    min_heap = list(freq.keys())
    heapq.heapify(min_heap)
    while min_heap:
        smallest = min_heap[0]
        for num in range(smallest, smallest + groupSize):
            if num not in freq:
                return False
            freq[num] -= 1

            if freq[num] == 0:
                if num != min_heap[0]:
                    return False
                heapq.heappop(min_heap)
    return True
print(isNStraightHand([1,1,1,1,2,3,6,2,3,4,7,8], 3))