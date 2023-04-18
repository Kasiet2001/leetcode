def findingUsersActiveMinutes(logs, k):
    from collections import Counter
    c = {}
    for i in logs:
        if i[0] in c:
            if i[1] not in c[i[0]]:
                c[i[0]].append(i[1])
            elif i[1] in c:
                continue
        else:
            c[i[0]] = [i[1]]
    am = [len(v) for k, v in c.items()]
    uam = Counter(am)
    d = [0] * k
    for u, m in uam.items():
        d[u - 1] = m
    return d
print(findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))