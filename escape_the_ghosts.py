def escapeGhosts(ghosts, target):
    human = abs(target[0]) + abs(target[1])
    for x, y in ghosts:
        if abs(target[0] - x) + abs(target[1] - y) <= human:
            return False
    return True
print(escapeGhosts([[1,0],[0,3]], [0,1]))