def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            candies[i] += candies[i - 1]
    for j in range(n - 2, -1, -1):
        if ratings[j + 1] < ratings[j]:
            candies[j] = max(candies[j], candies[j + 1] + 1)
    return candies
print(candy([1,3,2,2,1]))