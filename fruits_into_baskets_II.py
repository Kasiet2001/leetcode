def numOfUnplacedFruits(fruits, baskets):
    m = 0
    occupied = set()
    for fruit in fruits:
        for i in range(len(baskets)):
            if i not in occupied and baskets[i] >= fruit:
                m += 1
                occupied.add(i)
                break
    return len(baskets) - len(occupied)
print(numOfUnplacedFruits([4,2,5], [3,5,4]))