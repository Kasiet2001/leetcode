def kthFactor(n, k):
    f = []
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
            if len(f) == k:
                return f[-1]
    return -1
print(kthFactor(4, 4))