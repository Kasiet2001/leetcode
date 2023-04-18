def customSortString(order, s):
    order = order[::-1]
    cus = []
    for i in order:
        if i in s:
            cus.insert(0, i * s.count(i))
    for j in s:
        if j not in order:
            cus.append(j)
    return ''.join(cus)
print(customSortString("cbafg", "abcd"))
