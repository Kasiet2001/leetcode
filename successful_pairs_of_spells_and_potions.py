def successfulPairs(spells, potions, success):
    q = []
    potions.sort()
    a = len(potions)
    for i in spells:
        count = 0
        l = 0
        r = len(potions)
        x = success / i
        while l < r:
            mid = l + (r - l) // 2
            if potions[mid] >= x:
                r = mid
            else:
                l = mid + 1
        count = (a - l)
        q.append(count)
    return q
print(successfulPairs([15,8,19], [38,36,23], 328))