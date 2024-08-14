def findPrimePairs(n):
    prime = [i for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p] > 0:
            for i in range(p * p, n + 1, p):
                prime[i] = 0
        p += 1
    ans = []
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            ans.append([prime[i], prime[n - i]])
    return ans
print(findPrimePairs(10))