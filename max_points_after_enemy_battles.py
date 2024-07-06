def maximumPoints(enemyEnergies, currentEnergy):
    enemyEnergies.sort()
    if enemyEnergies[0] > currentEnergy:
        return 0
    currentEnergy += sum(enemyEnergies) - enemyEnergies[0]
    return currentEnergy // enemyEnergies[0]
print(maximumPoints([2], 10))
