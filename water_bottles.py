def numWaterBottles(numBottles, numExchange):
    ans = numBottles
    left = 0
    while numBottles // numExchange:
        left = numBottles % numExchange
        numBottles //= numExchange
        ans += numBottles
        numBottles += left
    return ans
print(numWaterBottles(15, 8))