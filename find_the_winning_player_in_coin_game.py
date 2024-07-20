def losingPlayer(x, y):
    move = 0
    while x and y >= 4:
        x -= 1
        y -= 4
        move += 1
    return 'Alice' if move % 2 else 'Bob'
print(losingPlayer(4, 11))