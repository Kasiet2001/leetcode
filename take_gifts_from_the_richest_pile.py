import heapq
def pickGifts(gifts, k):
    gifts = [-gift for gift in gifts]
    heapq.heapify(gifts)
    while k:
        gift = heapq.heappop(gifts)
        gift = -int((gift * -1) ** 0.5)
        heapq.heappush(gifts, gift)
        k -= 1
    return -sum(gifts)
print(pickGifts([54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,13,33,69,19,40,13,10,43,61,72], 7))
