def totalMoney(n):
    ans = 0
    money = 1
    for i in range(7, n + 7):
        if i % 7 == 0:
            money = i // 7
        ans += money
        money += 1
    return ans
print(totalMoney(4))