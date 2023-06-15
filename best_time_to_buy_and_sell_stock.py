def maxProfit(prices):
    ans = []
    buy = 0
    sell = 1
    while len(prices) > sell:
        if prices[sell] >= prices[buy]:
            ans.append(prices[sell] - prices[buy])
            sell += 1
        else:
            buy = sell
            sell += 1
    return max(ans) if len(ans) > 0 else 0
print(maxProfit([7,6,4,3,1]))
