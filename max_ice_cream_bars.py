def maxIceCream(costs, coins):
    if min(costs) > coins:
        return 0
    b = 0
    for i in sorted(costs):
        if coins - i >= 0:
            b += 1
        coins -= i
        if coins < i:
            break
    return b
print(maxIceCream([1,6,3,1,2,5], 18))