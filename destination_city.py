def destCity(paths):
    start = set()
    end = set()
    for s, e in paths:
        start.add(s)
        end.add(e)
    return list(end - start)[0]
print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))