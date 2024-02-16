def coinChange(coins, amount):
    dp = [0] + ([float('inf')] * amount)
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[-1] == float('inf'):
        return -1
    return dp[-1]
print(coinChange([1,2,5], 11))