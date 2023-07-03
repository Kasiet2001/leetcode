def findRelativeRanks(score):
    ans = []
    m = {s: p for p, s in enumerate(sorted(score, reverse=True), 1)}
    for i in score:
        if m[i] == 1:
            ans.append('Gold Medal')
        elif m[i] == 2:
            ans.append('Silver Medal')
        elif m[i] == 3:
            ans.append('Bronze Medal')
        else:
            ans.append(str(m[i]))
    return ans
print(findRelativeRanks([5,4,3,2,1]))