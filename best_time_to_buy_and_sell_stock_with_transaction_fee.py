def maxProfit(prices, fee):
    buy = float('-inf')
    sell = 0
    for price in prices:
        buy = max(buy, sell - price)
        sell = max(sell, buy - fee + price)
    return sell
print(maxProfit([1,3,2,8,4,9], 2))