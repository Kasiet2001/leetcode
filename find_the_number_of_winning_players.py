from collections import defaultdict
def winningPlayerCount(n, pick):
    balls = defaultdict(lambda: defaultdict(int))
    ans = set()
    for pl, ball in pick:
        balls[pl][ball] += 1
        if balls[pl][ball] > pl:
            ans.add(pl)
    return len(ans)
print(winningPlayerCount(2, [[0,8],[0,3]]))


