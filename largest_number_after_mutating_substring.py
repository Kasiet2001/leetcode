def maximumNumber(num, change):
    n = list(num)
    flag = False
    for i, ch in enumerate(n):
        x = int(ch)
        if x < change[x]:
            n[i] = str(change[x])
            flag = True
        elif x > change[x] and flag:
            break
    return ''.join(n)
print(maximumNumber("132", [9,8,5,0,3,6,4,2,6,8]))