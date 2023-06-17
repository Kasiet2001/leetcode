def minimumCardPickup(cards):
    ans = len(cards)
    d = {}
    for i in range(len(cards)):
        if cards[i] in d:
            ans = min(ans, i - d[cards[i]])
            d[cards[i]] = i
        else:
            d[cards[i]] = i
    return ans + 1 if len(d) < len(cards) else -1
print(minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]))