def maxCoins(piles):
    res = 0
    piles.sort()
    for i in range(len(piles) // 3):
        res += piles[-2 - 2 * i]
    return res
print(maxCoins([9,8,7,6,5,1,2,3,4]))