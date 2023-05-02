def canPlaceFlowers(flowerbed, n):
    i = 0
    a = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            a += 1
        if a >= n:
            return True
        i += 1
    return False
print(canPlaceFlowers([1,0,0,0,1], 2))