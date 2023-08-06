def accountBalanceAfterPurchase(purchaseAmount):
    return 100 - (purchaseAmount + 5) // 10 * 10
print(accountBalanceAfterPurchase(11))