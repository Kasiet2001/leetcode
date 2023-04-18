def equalFrequency(word):
    n = [word.count(i) for i in set(word)]
    if len(set(n)) == 1 and n.count(1) == len(n):
        return True
    if n.count(1) == 1 and len(set(n)) == 2:
        return True
    for i in range(len(n)):
        n[i] = n[i] - 1
        if len(set(n)) == 1:
            return True
        else:
            n[i] = n[i] + 1
    return False

print(equalFrequency("aazz"))