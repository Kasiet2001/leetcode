def minChanges(n, k):
    n = bin(n)[2:]
    k = bin(k)[2:]
    k = '0' * (len(n) - len(k)) + k
    changes = 0
    if len(n) == len(k):
        for i in range(len(n)):
            if n[i] == '1' and k[i] == '0':
                changes += 1
            elif n[i] == '0' and k[i] == '1':
                return -1
        return changes
    return -1
print(minChanges(2, 47))
