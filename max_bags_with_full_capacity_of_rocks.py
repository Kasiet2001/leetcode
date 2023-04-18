def maximumBags(capacity, rocks, additionalRocks):
    res = 0
    for i in range(len(capacity)):
        capacity[i] = capacity[i] - rocks[i]
    capacity.sort()
    for i in capacity:
        if additionalRocks - i >= 0:
            res += 1
            additionalRocks -= i
    return res
print(maximumBags([91,54,63,99,24,45,78], [35,32,45,98,6,1,25], 17))