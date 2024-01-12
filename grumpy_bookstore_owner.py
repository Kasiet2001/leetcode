def maxSatisfied(customers, grumpy, minutes):
    satisfied = 0
    not_satisfied = 0
    flag = False
    for i in range(len(customers)):
        if not grumpy[i]:
            satisfied += customers[i]
            customers[i] = 0
    curr = 0
    for i, cust in enumerate(customers):
        curr += customers[i]
        if i >= minutes:
            curr -= customers[i - minutes]
        not_satisfied = max(curr, not_satisfied)
    return satisfied + not_satisfied
print(maxSatisfied([4,2,5,7], [0,1,1,1], 2))