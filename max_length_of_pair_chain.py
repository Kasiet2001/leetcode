def findLongestChain(pairs):
    pairs = sorted(pairs, key=lambda x: x[1])
    cur = pairs[0][1]
    ans = 1
    for i in range(1, len(pairs)):
        if pairs[i][0] > cur:
            cur = pairs[i][1]
            ans += 1
    return ans
print(findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))
