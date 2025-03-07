def closestPrimes(left, right):
    def SieveOfEratosthenes(n):
        prime = [True for i in range(n + 1)]
        prime[0] = prime[1] = False
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return prime
    sieve = SieveOfEratosthenes(right)
    prime_nums = [num for num in range(left, right + 1) if sieve[num]]
    if len(prime_nums) < 2:
        return -1, -1
    min_diff = float('inf')
    ans = [-1, -1]
    for i in range(1, len(prime_nums)):
        diff = prime_nums[i] - prime_nums[i - 1]
        if diff < min_diff:
            min_diff = diff
            ans = prime_nums[i - 1], prime_nums[i]
    return ans
print(closestPrimes(10, 19))
