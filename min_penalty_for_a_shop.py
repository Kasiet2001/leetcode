def bestClosingTime(customers):
    l = len(customers)
    Y = customers.count('Y')
    min_p = l
    no_cus = 0
    cus = 0
    for i in range(l + 1):
        y = Y - cus
        p = y + no_cus
        if p < min_p:
            h = i
            min_p = p
        cus += (1 if i < l and customers[i] == 'Y' else 0)
        no_cus += (1 if i < l and customers[i] == 'N' else 0)
    return h
print(bestClosingTime("YYNY"))
