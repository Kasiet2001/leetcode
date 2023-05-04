def predictPartyVictory(senate):
    l = len(senate)
    radiants = [i for i in range(l) if senate[i] == 'R']
    dires = [i for i in range(l) if senate[i] == 'D']
    while radiants and dires:
        r = radiants.pop(0)
        d = dires.pop(0)
        if r < d:
            radiants.append(l + r)
        else:
            dires.append(l + d)
    return 'Radiant' if radiants else 'Dire'
print(predictPartyVictory("RDD"))