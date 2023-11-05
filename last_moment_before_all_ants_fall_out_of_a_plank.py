def getLastMoment(n, left, right):
    ans = 0
    for i in left:
        ans = max(ans, i)
    for j in right:
        ans = max(ans, abs(n - j))
    return ans 
