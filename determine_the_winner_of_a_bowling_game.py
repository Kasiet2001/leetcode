def isWinner(player1, player2):
    player1.extend([0, 0])
    player2.extend([0, 0])
    p1, p2 = 0, 0
    for i in range(len(player1) - 2):
        if player1[i - 1] == 10 or player1[i - 2] == 10:
            p1 += player1[i] * 2
        else:
            p1 += player1[i]
        if player2[i - 1] == 10 or player2[i - 2] == 10:
            p2 += player2[i] * 2
        else:
            p2 += player2[i]
    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    return 0
print(isWinner([5,6,1,10], [5,1,10,5]))