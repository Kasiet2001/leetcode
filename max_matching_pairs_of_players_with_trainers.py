def matchPlayersAndTrainers(players, trainers):
    players.sort()
    trainers.sort()
    p = len(players) - 1
    t = len(trainers) - 1
    ans = 0
    while p > -1 and t > -1:
        if players[p] > trainers[t]:
            p -= 1
        elif players[p] <= trainers[t]:
            ans += 1
            p -= 1
            t -= 1
    return ans
print(matchPlayersAndTrainers([1,1,1], [10]))
