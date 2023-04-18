def reconstructQueue(people):
    res = []
    q = sorted(people, key=lambda x: (-x[0], x[1]))
    for p in q:
        res.insert(p[1], p)
    return res
print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))