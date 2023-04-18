def minimumRefill(plants, capacityA, capacityB):
    if len(plants) == 1:
        return 0
    a, b = 0, len(plants) - 1
    aliceCan, bobCan = capacityA, capacityB
    refills = 0
    while a <= b:
        if a == b:
            if aliceCan >= bobCan:
                if aliceCan < plants[a]:
                    refills += 1
                a += 1
            else:
                if bobCan < plants[b]:
                    refills += 1
                b -= 1
        else:
            if aliceCan < plants[a]:
                aliceCan = capacityA
                refills += 1
            aliceCan -= plants[a]
            a += 1
            if bobCan < plants[b]:
                bobCan = capacityB
                refills += 1
            bobCan -= plants[b]
            b -= 1
    return refills
print(minimumRefill([1,10,1], 10, 11))

