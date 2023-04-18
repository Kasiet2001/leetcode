def sortPeople(names, heights):
    d = {}
    for i in range(len(heights)):
        d[heights[i]] = names[i]
    s = sorted(d.items(), reverse=True)
    return [i[1] for i in s]
print(sortPeople( ["Alice","Bob","Bob"],[155,185,150]))