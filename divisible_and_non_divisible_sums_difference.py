def differenceOfSums(n, m):
    ans = 0
    for i in range(1, n + 1):
        if i % m == 0:
            ans -= i
        else:
            ans += i
    return ans
print(differenceOfSums(5, 6))