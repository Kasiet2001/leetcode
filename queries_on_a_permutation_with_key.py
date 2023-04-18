def processQueries(queries, m):
    ind = []
    p = [i for i in range(1, m + 1)]
    for i in queries:
        ind.append(p.index(i))
        p.remove(i)
        p.insert(0, i)
    return ind
print(processQueries([7,5,5,8,3], 8))