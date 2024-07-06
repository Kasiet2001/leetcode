def numberOfAlternatingGroups(colors):
    colors.extend(colors[:2])
    n = len(colors)
    count = 0

    for i in range(1, n - 1):
        if colors[i - 1] != colors[i] and colors[i] != colors[i + 1]:
            count += 1
    return count


print(numberOfAlternatingGroups([0,1,0,0,1]))