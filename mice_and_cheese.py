def miceAndCheese(reward1, reward2, k):
    diff = {i: reward1[i] - reward2[i] for i in range(len(reward1))}
    ans = 0
    eaten = {}
    sort_diff = sorted(diff.items(), key=lambda x: x[1], reverse=True)
    for i in range(k):
        ind = sort_diff[i][0]
        ans += reward1[ind]
        eaten[ind] = 1
    for i in range(len(reward2)):
        if eaten.get(i) != None:
            continue
        else:
            ans += reward2[i]
    return ans
print(miceAndCheese([3,3,1,1], [4,4,1,1], 2))