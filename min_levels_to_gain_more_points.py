def minimumLevels(possible):
    ones = sum(possible)
    total = ones - (len(possible) - ones)
    bob = 0
    for i in range(len(possible)):
        if possible[i] == 1:
            bob += 1
            total -= 1
        else:
            bob -= 1
            total += 1
        if bob > total:
            return i + 1
    return -1
print(minimumLevels([0,0,0]))