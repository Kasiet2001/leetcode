def countPrimes(n):
    prime = [True for i in range(n)]
    ans = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            ans += 1
    return ans
print(countPrimes(10))