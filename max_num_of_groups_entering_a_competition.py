def maximumGroups(grades):
    n = len(grades)
    g = 0
    while n >= g + 1:
        g += 1
        n -= g
    return g
print(maximumGroups([2,31,41,31,36,46,33,45,47,8,31,6,12,12,15,35]))
