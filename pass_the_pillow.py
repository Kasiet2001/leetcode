def passThePillow(n, time):
    flag = False
    idx = 0
    for i in range(time):
        if not flag:
            idx += 1
        elif flag:
            idx -= 1
        if n - 1 == idx:
            flag = True
        elif idx == 0:
            flag = False
    return idx + 1
print(passThePillow(4, 5))


