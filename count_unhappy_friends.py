def unhappyFriends(n, preferences, pairs):
    bf = {}
    ans = 0
    for x, y in pairs:
        bf[x] = preferences[x][:preferences[x].index(y)]
        bf[y] = preferences[y][:preferences[y].index(x)]
    for i in bf:
        for j in bf[i]:
            if i in bf[j]:
                ans += 1
                break
    return ans
print(unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]))
