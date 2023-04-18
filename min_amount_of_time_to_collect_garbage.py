def garbageCollection(garbage, travel):
    t = 0
    for i in ['M', 'P', 'G']:
        k = 0
        for j in range(len(garbage)):
            t += garbage[j].count(i)
            if i in garbage[j]:
                k = j
        t += sum(travel[:k])
    return t
print(garbageCollection(["MMM","PGM","GP"], [3,10]))