def numberOfEmployeesWhoMetTarget(hours, target):
    return sum(hours >= target for hours in hours)
print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))