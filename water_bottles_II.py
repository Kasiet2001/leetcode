def maxBottlesDrunk(numBottles, numExchange):
    drunk = 0
    while numExchange > 0:
        if numBottles < numExchange:
            return drunk + numBottles
        drunk += numExchange
        numBottles -= numExchange - 1
        numExchange += 1
    return drunk
print(maxBottlesDrunk(20, 1))