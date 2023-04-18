def findWinners(matches):
    from collections import Counter
    w = [i[0] for i in matches]
    l = [j[1] for j in matches]
    losers = []
    winners = list(set(w) - set(l))
    n = Counter(l)
    for k, v in n.items():
        if v == 1:
            losers.append(k)
    return [sorted(winners), sorted(losers)]
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))