def numSpecial(mat):
    col = list(zip(*mat))
    ans = 0
    for i in range(len(mat)):
        if mat[i].count(1) == 1:
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and col[j].count(1) == 1:
                    ans += 1
    return ans
print(numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]))