def numOfBurgers(tomatoSlices, cheeseSlices):
    if tomatoSlices < 2 * cheeseSlices:
        return []
    elif tomatoSlices % 2:
        return []
    jumbo = (tomatoSlices // 2 - cheeseSlices)
    small = cheeseSlices - jumbo
    if jumbo < 0 or small < 0:
        return []
    return [jumbo, small]
print(numOfBurgers(16, 7))
