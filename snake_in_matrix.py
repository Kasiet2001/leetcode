def finalPositionOfSnake(n, commands):
    ans = 0
    for c in commands:
        if c == 'UP':
            ans -= n
        elif c == 'DOWN':
            ans += n
        elif c == 'RIGHT':
            ans += 1
        else:
            ans -= 1
    return ans
print(finalPositionOfSnake(3, ["DOWN","RIGHT","UP"]))