def maxEnergyBoost(energyDrinkA, energyDrinkB):
    n = len(energyDrinkA)
    if n == 0:
        return 0

    dpA = [0] * n
    dpB = [0] * n

    dpA[0] = energyDrinkA[0]
    dpB[0] = energyDrinkB[0]

    if n > 1:
        dpA[1] = max(energyDrinkA[0] + energyDrinkA[1], energyDrinkB[0])
        dpB[1] = max(energyDrinkB[0] + energyDrinkB[1], energyDrinkA[0])

    for i in range(2, n):
        dpA[i] = max(dpA[i - 1] + energyDrinkA[i], dpB[i - 2] + energyDrinkA[i])
        dpB[i] = max(dpB[i - 1] + energyDrinkB[i], dpA[i - 2] + energyDrinkB[i])

    return max(dpA[-1], dpB[-1])
print(maxEnergyBoost([1,3,1], [1,1,3]))
