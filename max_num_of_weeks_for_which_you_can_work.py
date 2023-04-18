def numberOfWeeks(milestones):
    summ = sum(milestones)
    maximum = max(milestones)
    if summ - maximum >= maximum:
        return summ
    return 2 * (summ - maximum) + 1
print(numberOfWeeks([5,2,1]))