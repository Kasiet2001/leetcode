def change(amount, coins):
    ways = [0 for _ in range(amount + 1)]
    ways[0] = 1
    for i in coins:
        for j in range(1, len(ways)):
            if i <= j:
                ways[j] += ways[j - i]
    return ways[len(ways) - 1]
print(change(5, [1,2,5]))
