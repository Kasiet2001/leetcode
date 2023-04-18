def wateringPlants(plants, capacity):
    res = 0
    cap = capacity
    for i, p in enumerate(plants):
        if p > cap:
            res += i * 2
            cap = capacity
        res += 1
        cap -= p
    return res
print(wateringPlants([1,1,1,4,2,3], 4))