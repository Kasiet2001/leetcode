def findCenter(edges):
    for i in edges[0]:
        n = 0
        for j in edges:
            if i in j:
                n += 1
        if n == len(edges):
            return i
print(findCenter([[1,2],[5,1],[1,3],[1,4]]))
