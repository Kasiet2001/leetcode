def findSmallestSetOfVertices(n, edges):
    m = [0] * n
    ans = []
    for i in edges:
        m[i[1]] += 1
    for j in range(n):
        if m[j] == 0:
            ans.append(j)
    return ans
print(findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))
