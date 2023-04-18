def bestHand(ranks, suits):
    if len(set(suits)) == 1:
        return 'Flush'
    r = [ranks.count(i) for i in set(ranks)]
    if max(r) >= 3:
        return 'Three of a Kind'
    elif max(r) >= 2:
        return 'Pair'
    return 'High Card'
print(bestHand([4,4,2,4,4],["d","a","a","b","c"]))