def distributeCandies(candyType):
    alice_can_eat = len(candyType) // 2
    type_of_candies = len(set(candyType))
    return min(alice_can_eat, type_of_candies)
print(distributeCandies([1,1,2,2,3,3]))