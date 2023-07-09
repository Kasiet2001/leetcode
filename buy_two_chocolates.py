def buyChoco(prices, money):
    prices.sort()
    ans = money - prices[0] - prices[1]
    return money if ans < 0 else ans
print(buyChoco([3,2,3], 3))