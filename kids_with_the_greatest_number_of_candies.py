def kidsWithCandies(candies, extraCandies):
    return [True if i + extraCandies >= max(candies) else False for i in candies]
print(kidsWithCandies([4,2,1,1,2], 1))