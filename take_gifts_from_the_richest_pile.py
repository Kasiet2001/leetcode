def pickGifts(gifts, k):
    from math import floor
    i = 0
    while i < k:
        gifts.sort()
        s = floor(gifts[-1] ** 0.5)
        gifts[-1] = s
        i += 1
    return sum(gifts)
print(pickGifts([25,64,9,4,100], 4))
